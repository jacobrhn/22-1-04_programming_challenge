from import_data_ex import DataLoader
import pandas as pd


class ETL:
    final_table = pd.DataFrame()

    def __init__(self, data_specs=None):
        self.importer = DataLoader(data_specs)
        self.load_data()
        """self.return_raw_sales_code_df()
        self.return_raw_engines_table_df()"""
        self.return_raw_vehicle_hash_df()

    def run(self):
        self.enhance_raw_data()
        self.create_final_table()
        self.save_final_table()
        return self.final_table

    def save_final_table(self):
        database_path = self.importer.database_config["database_path"]
        # your code here #

    def create_final_table(self):
        self.raw_data_tables["sales_codes"] = self.raw_data_tables["sales_codes"].drop(columns=['Unnamed: 0'])
        self.raw_data_tables["vehicle_hash"] = self.raw_data_tables["vehicle_hash"].drop(
            columns=['Unnamed: 0', 'record_source', 'load_ts'])
        # self.raw_data_tables["engines"] = self.raw_data_tables["engines"].drop(columns=[TOBECONTINUED])

    def enhance_raw_data(self):
        self.handle_nans()
        self.handle_invalid_fins()
        self.handle_invalid_dates()

    def handle_invalid_dates(self):
        self.raw_data_tables["sales_codes"]["production_date"] = pd.to_datetime(self.raw_data_tables["sales_codes"]["production_date"],
                                                                                dayfirst=True, errors='coerce')

    def handle_invalid_fins(self, num_of_digits_in_fin=17):
        for row in self.raw_data_tables["vehicle_hash"].index:
            if len(str(self.raw_data_tables["vehicle_hash"].loc[row, "fin"])) != num_of_digits_in_fin:
                self.raw_data_tables["vehicle_hash"].drop(row, inplace=True)
        # implement reset index

    def handle_nans(self):
        self.raw_data_tables["sales_codes"].dropna(subset=
                                                   ("h_vehicle_hash", "production_date", "country", "sales_code_array"),
                                                   axis=0, inplace=True)
        #implement reset index

    def load_data(self):
        self.raw_data_tables = self.importer.load_data()

    """def return_raw_sales_code_df(self):
        self.raw_sales_code_df = self.raw_data_tables["sales_codes"]
    
    def return_raw_engines_table_df(self):
        self.raw_engines_df = self.raw_data_tables["engines"]"""

    def return_raw_vehicle_hash_df(self):
        self.raw_vehicle_hash_df = self.raw_data_tables["vehicle_hash"].drop(columns=['Unnamed: 0', 'record_source', 'load_ts'])
