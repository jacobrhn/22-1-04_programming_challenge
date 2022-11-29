import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


class DataFilter:
    def __init__(self, data_frame: pd.DataFrame, date_lower: str = None, date_upper: str = None):
        self.data_to_filter = data_frame
        self.date_lower = pd.to_datetime(date_lower, dayfirst=True)
        self.date_upper = pd.to_datetime(date_upper, dayfirst=True)

    def for_dates(self):
        for row in self.data_to_filter.index:
            if not self.date_lower <= self.data_to_filter.loc[row, "production_date"] <= self.date_upper:
                self.data_to_filter.drop(row, inplace=True)
        return self.data_to_filter # .swapaxes(axis1=0, axis2=1, copy=True)


class Analyser:
    def __init__(self, table, figure_save_path, filter: DataFilter):
        self.figure_save_path = figure_save_path
        self.final_table = table
        self.filter = filter

    def run(self):
        self.visualize_sales_per_countries()
        self.visualize_sales_per_year()

    def sales_top_three_countries(self):
        filter


    def filter_for_years(self, date_lower: str = None, date_upper: str = None):
        self.date_lower = pd.to_datetime(date_lower, dayfirst=True)
        self.date_upper = pd.to_datetime(date_upper, dayfirst=True)
        df = self.final_table
        df["counter"] = 1
        for row in df.index:
            if not self.date_lower <= df.loc[row, "production_date"] <= self.date_upper:
                df.drop(row, inplace=True)
            return df

    def visualize_sales_per_countries(self):
        # your code here #
        pass

    def visualize_sales_per_year(self):
        # your code here #
        pass
