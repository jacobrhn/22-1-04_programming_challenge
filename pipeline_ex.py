import os
from datetime import datetime

from import_data_ex import DataLoader
import pandas as pd

pd.set_option('display.max_columns', 5)


class ETL:
    final_table = pd.DataFrame()

    def __init__(self, data_specs=None):
        self.importer = DataLoader(data_specs)
        self.load_data()

    def run(self):
        self.enhance_raw_data()
        self.create_final_table()
        self.save_final_table()
        return self.final_table

    def save_final_table(self):
        database_path = self.importer.database_config["database_path"]
        data_file_name = "enhanced_vehicle_data.xlsx"
        self.final_table.to_excel(os.path.join(database_path, data_file_name))

    def create_final_table(self):
        self.raw_data_tables["sales_codes"] = self.raw_data_tables["sales_codes"].drop(columns=['Unnamed: 0'])
        self.raw_data_tables["vehicle_hash"] = self.raw_data_tables["vehicle_hash"].drop(
            columns=['Unnamed: 0', 'record_source', 'load_ts'])
        self.final_table = pd.merge(self.raw_data_tables["sales_codes"],
                                    self.raw_data_tables["vehicle_hash"],
                                    on="h_vehicle_hash").drop(columns=["h_vehicle_hash"])
        self.final_table = self.final_table[["fin", "production_date", "country", "sales_code_array"]]

    def enhance_raw_data(self):
        self.handle_nans()
        self.handle_invalid_fins()
        self.handle_invalid_dates()
        self.sales_code_to_vehicle_code()

    def handle_invalid_dates(self):
        date_lower = datetime(2011, 1, 1, 00, 00, 00)
        date_upper = datetime(2021, 12, 31, 23, 59, 59)

        self.raw_data_tables["sales_codes"]["production_date"] = pd.to_datetime(
            self.raw_data_tables["sales_codes"]["production_date"],
            dayfirst=True, errors='coerce')

        for row in self.raw_data_tables["sales_codes"].index:
            if not self.raw_data_tables["sales_codes"].loc[row, "production_date"]:
                self.raw_data_tables["sales_codes"].drop(row, inplace=True)
            if not date_lower <= self.raw_data_tables["sales_codes"].loc[row, "production_date"] <= date_upper:
                self.raw_data_tables["sales_codes"].drop(row, inplace=True)


        # remove timestamp dt.datetime.strptime(start_date, "%d.%m.%Y")

    def handle_invalid_fins(self, num_of_digits_in_fin=17):
        for row in self.raw_data_tables["vehicle_hash"].index:
            if len(str(self.raw_data_tables["vehicle_hash"].loc[row, "fin"])) != num_of_digits_in_fin:
                self.raw_data_tables["vehicle_hash"].drop(row, inplace=True)

    def handle_nans(self):
        self.raw_data_tables["sales_codes"].dropna(axis=0, inplace=True)

    def sales_code_to_vehicle_code_0(self):
        """for row in self.raw_data_tables["sales_codes"].index:
            motor_code = row["sales_code_array"][0:3]
            if motor_code == "Z5E":
                row["sales_code_array"] = "OM471"""
        # self.raw_data_tables["sales_codes"]["sales_code_array"].replace(to_replace=["sales_code_array"][0:3] == "Z5E", value="OM471", inplace=True)
        pass

    def sales_code_to_vehicle_code(self):
        """result = 1
        for row in self.raw_data_tables["sales_codes"]["sales_code_array"].items():
            if row[0:3] == "Z5C": # self.raw_data_tables["engines"]["Sales Code"]:
                result =  True # row["engine_type"] = "OM 471"
            return result"""
        pass

    def load_data(self):
        self.raw_data_tables = self.importer.load_data()
