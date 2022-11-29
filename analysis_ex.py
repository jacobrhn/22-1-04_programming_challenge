import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


class DataFilter:
    def __init__(self, data_frame: pd.DataFrame, date_lower: str = None, date_upper: str = None):
        self.filtered_data = pd.DataFrame(data=data_frame)
        self.__date_lower = pd.to_datetime(date_lower, dayfirst=True)
        self.__date_upper = pd.to_datetime(date_upper, dayfirst=True)
        #self.for_dates()

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

    def data_sales_top_three_countries(self):
        filter_2014_2020 = DataFilter(data_frame=self.final_table, date_lower="1.1.2014", date_upper="31.12.2021")
        data_2014_2020 = filter_2014_2020.for_dates().groupby(by=["country"]).count().sort_values(by=["fin", "country"], ascending=False)
        #counter_2014_2020 = data_2014_2020.groupby(["country"]).count().sort_values(by="country")
        return data_2014_2020.drop(columns=["fin", "production_date", "sales_code_array"]).iloc[[0,1,2]]
        #return counter.sort_values(by="counter", ascending=False)




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
