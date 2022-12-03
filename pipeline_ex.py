import os
import pandas as pd
from datetime import datetime as dt
from import_data_ex import DataLoader


class ETL:
    final_table = pd.DataFrame()

    def __init__(self, data_specs=None):
        self.importer = DataLoader(data_specs)
        self.__load_data()

    def __load_data(self):
        self.raw_data = self.importer.load_data()
        self.raw_sales_codes = self.raw_data["sales_codes"]
        self.raw_vehicle_hash = self.raw_data["vehicle_hash"]

    def __enhance_dates(self):
        date_lower = dt(2011, 1, 1, 00, 00, 00)
        date_upper = dt(2021, 12, 31, 23, 59, 59)
        self.raw_sales_codes["production_date"] = pd.to_datetime(
            self.raw_sales_codes["production_date"],
            dayfirst=True, errors='coerce')
        for row in self.raw_sales_codes.index:
            if not self.raw_sales_codes.loc[row, "production_date"]:
                self.raw_sales_codes.drop(row, inplace=True)
            if not date_lower <= self.raw_sales_codes.loc[row, "production_date"] <= date_upper:
                self.raw_sales_codes.drop(row, inplace=True)

    def __enhance_fins(self):
        for row in self.raw_vehicle_hash.index:
            if len(str(self.raw_vehicle_hash.loc[row, "fin"])) != 17:
                self.raw_vehicle_hash.drop(row, inplace=True)

    def __remove_nans(self):
        self.raw_sales_codes.dropna(axis=0, inplace=True)

    def __add_counter_and_motor_code(self):
        self.raw_sales_codes["counter"] = 1
        dict_engine_sales_codes = {"Z5B": "OM 934", "Z5C": "OM 936", "Z5D": "OM 470",
                                   "Z5E": "OM 471", "Z5F": "OM 473", "Z5L": "OM 460"}
        for row in self.raw_sales_codes.index:
            self.raw_sales_codes.loc[row, "motor_type"] = self.raw_sales_codes["sales_code_array"][row][0:3]
            for key, value in dict_engine_sales_codes.items():
                if self.raw_sales_codes.loc[row, "motor_type"] == key:
                    self.raw_sales_codes.loc[row, "motor_type"] = value

    def __enhance_raw_data(self):
        self.__remove_nans()
        self.__enhance_fins()
        self.__enhance_dates()
        self.__add_counter_and_motor_code()

    def __create_final_df(self):
        self.final_table = pd.merge(self.raw_sales_codes, self.raw_vehicle_hash, on="h_vehicle_hash") \
            .drop(columns=["h_vehicle_hash", "sales_code_array", 'record_source', 'load_ts'])
        self.final_table = self.final_table[["fin", "production_date", "country", "motor_type", "counter"]]

    def __save_final_df(self):
        database_path = self.importer.database_config["database_path"]
        data_file_name = "enhanced_vehicle_data.xlsx"
        self.final_table.to_excel(os.path.join(database_path, data_file_name))

    def run(self):
        self.__enhance_raw_data()
        self.__create_final_df()
        self.__save_final_df()
        return self.final_table
