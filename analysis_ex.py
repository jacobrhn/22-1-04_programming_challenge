import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


class DataFilter:
    def __init__(self, data_frame: pd.DataFrame, date_lower: str = None, date_upper: str = None):
        self.data = data_frame
        self.__date_lower = pd.to_datetime(date_lower)
        self.__date_upper = pd.to_datetime(date_upper)

    def for_dates(self):
        dict_data_filtered = {}
        df_data_filtered = pd.DataFrame(data=dict_data_filtered)
        for row in self.data.index:
            if self.__date_lower <= self.data.loc[row, "production_date"] <= self.__date_upper:
                df_data_filtered.concat(self.data.loc[row])
        return df_data_filtered


class Analyser:
    def __init__(self, table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table
        self.filter_for_years()

    def run(self):
        self.visualize_sales_per_countries()
        self.visualize_sales_per_year()

    def sales_top_three_countries(self):
        date_lower = datetime(2014, 1, 1, 00, 00, 00)
        date_upper = datetime(2020, 12, 31, 00, 00, 00)
        dict_data_to_visualize = {"fin", "production_date", "country", "sales_code_array"}
        df_data_to_visualize = pd.DataFrame(data=dict_data_to_visualize)
        for row in self.final_table.index:
            if date_lower <= self.final_table.loc[row, "production_date"] <= date_upper:
                df_data_to_visualize[len(df_data_to_visualize.index)] = self.final_table.loc[row]
        return df_data_to_visualize

    def filter_for_years(self):
        df = self.final_table
        df["counter"] = 1
        # your code here #

    def visualize_sales_per_countries(self):
        # your code here #
        pass

    def visualize_sales_per_year(self):
        # your code here #
        pass
