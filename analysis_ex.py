import pandas as pd
import matplotlib as plt

class Analyser:
    def __init__(self, table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table

    def run(self):
        self.visualize_sales_per_countries()
        self.visualize_sales_per_year()

    def filter_for_years(self, date_lower: str = None, date_upper: str = None):
        date_lower = pd.to_datetime(date_lower, dayfirst=True)
        date_upper = pd.to_datetime(date_upper, dayfirst=True)
        df_in_date_range = self.final_table
        for row in df_in_date_range.index:
            if not pd.to_datetime(date_lower, dayfirst=True) <= df_in_date_range.loc[row, "production_date"] <= pd.to_datetime(date_upper, dayfirst=True):
                df_in_date_range.drop(row, inplace=True)
        return df_in_date_range.reset_index(drop=True)

    def df_sales_top_three_countries(self, date_lower: str, date_upper: str):
        return self.filter_for_years(date_lower=date_lower, date_upper=date_upper) \
            .groupby(by=["country"]).count()\
            .sort_values(by=["fin", "country"], ascending=False)\
            .drop(columns=["fin", "production_date", "motor_type"])\
            .iloc[[0, 1, 2]]

    def df_sales_by_year(self, date_lower: str, date_upper: str):
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        df_in_date_range.loc[:, "production_year"] = pd.DatetimeIndex(df_in_date_range.loc[:, "production_date"]).year
        return df_in_date_range.groupby(by="production_year").count().sort_values(by="counter", ascending=False) \
            .drop(columns=["fin", "production_date", "country", "motor_type"])

    def df_fins_sorted_dates(self):
        return self.final_table.sort_values(by="production_date").drop(columns=["country", "counter", "motor_type"])

    def df_vehicles_by_motor_types(self, date_lower: str, date_upper: str, motors_list: list):
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "motor_type"] in motors_list:
                df_in_date_range.drop(row, inplace=True)
        return df_in_date_range.groupby(by="motor_type").count().drop(columns=["fin", "country", "production_date"])

    def df_vehicles_by_motor_types_country(self, date_lower: str, date_upper: str, motors_list: list, country: str):
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "motor_type"] in motors_list:
                df_in_date_range.drop(row, inplace=True)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "country"] == country:
                df_in_date_range.drop(row, inplace=True)
        return df_in_date_range["fin"]

    def visualize_sales_per_countries(self):
        # your code here #
        pass

    def visualize_sales_per_year(self):
        # your code here #
        pass