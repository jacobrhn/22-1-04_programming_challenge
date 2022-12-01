import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


class DataFilter:
    def __init__(self, data_frame: pd.DataFrame, date_lower: str = None, date_upper: str = None):
        self.filtered_data = pd.DataFrame(data=data_frame)
        self.__date_lower = pd.to_datetime(date_lower, dayfirst=True)
        self.__date_upper = pd.to_datetime(date_upper, dayfirst=True)
        # self.for_dates()

    def for_dates(self):
        for row in self.filtered_data.index:
            if not self.__date_lower <= self.filtered_data.loc[row, "production_date"] <= self.__date_upper:
                self.filtered_data.drop(row, inplace=True)
        return self.filtered_data.reset_index(drop=True)


class Analyser:
    def __init__(self, table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table
        self.filter_for_years()

    def run(self):
        self.visualize_sales_per_countries()
        self.visualize_sales_per_year()

    def df_with_date_range(self, date_lower: str, date_upper: str):
        filtered_data = DataFilter(data_frame=self.final_table, date_lower=date_lower, date_upper=date_upper)
        return filtered_data.for_dates()

    def df_sales_top_three_countries(self, date_lower: str, date_upper: str):
        return self.df_with_date_range(date_lower=date_lower, date_upper=date_upper)\
            .groupby(by=["country"]) \
            .count().sort_values(by=["fin", "country"], ascending=False) \
            .drop(columns=["fin", "production_date", "counter"]).iloc[[0, 1, 2]]

    def df_sales_top_country(self, date_lower: str, date_upper: str):
        date_filter = DataFilter(data_frame=self.final_table, date_lower=date_lower, date_upper=date_upper)
        df_filtered_data = date_filter.for_dates()
        df_filtered_data.loc[:, "production_year"] = pd.DatetimeIndex(df_filtered_data.loc[:, "production_date"]).year
        return df_filtered_data.groupby(by="production_year").count().sort_values(by="counter", ascending=False)\
            .drop(columns=["fin", "production_date", "country", "sales_code_array"])

    def df_first_fin(self):
        return self.final_table.sort_values(by="production_date").drop(columns=["country", "sales_code_array", "counter"])

    def df_vehicles_by_motor_types(self, date_lower: str, date_upper: str):
        date_filter = DataFilter(data_frame=self.final_table, date_lower=date_lower, date_upper=date_upper)
        df_filtered_data = date_filter.for_dates()
        #df_filtered_data.loc[:, "sales_code_array"] = df_filtered_data
        pass


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
