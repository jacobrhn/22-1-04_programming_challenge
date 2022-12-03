import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class Analyser:
    def __init__(self, table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table

    def filter_for_years(self, date_lower: str = None, date_upper: str = None):
        date_lower = pd.to_datetime(date_lower, dayfirst=True)
        date_upper = pd.to_datetime(date_upper, dayfirst=True)
        df_in_date_range = self.final_table
        for row in df_in_date_range.index:
            if not pd.to_datetime(date_lower, dayfirst=True) <= df_in_date_range.loc[row, "production_date"] <= pd.to_datetime(date_upper, dayfirst=True):
                df_in_date_range.drop(row, inplace=True)
        return df_in_date_range.reset_index(drop=True)

    def df_sales_top_three_countries(self, date_lower: str, date_upper: str):
        title = f"Top Three: sold vehicles per country "\
                f"({pd.to_datetime(date_lower, dayfirst=True).year}-{pd.to_datetime(date_upper, dayfirst=True).year})"
        df_filtered_grouped_counted = self.filter_for_years(date_lower=date_lower, date_upper=date_upper) \
            .groupby(by=["country"]).count()\
            .sort_values(by=["fin", "country"], ascending=False)\
            .drop(columns=["fin", "production_date", "motor_type"])\
            .iloc[[0, 1, 2]]
        df_filtered_grouped_counted.plot(use_index=True, y=["counter"], kind="bar", color="gray")
        plt.title(title)
        plt.legend().set_visible(False)
        plt.xlabel("Country")
        plt.xticks(rotation=0)
        plt.ylabel("Sold Vehicles (pc.)")
        plt.grid(axis="y")
        plt.savefig(self.figure_save_path + "countries.png")
        print("________________________________________________________")
        print(title)
        print(df_filtered_grouped_counted)

    def df_sales_by_year(self, date_lower: str, date_upper: str):
        title = f"Sold vehicles per year "\
                f"({pd.to_datetime(date_lower, dayfirst=True).year}-{pd.to_datetime(date_upper, dayfirst=True).year})"
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        df_in_date_range.loc[:, "production_year"] = pd.DatetimeIndex(df_in_date_range.loc[:, "production_date"]).year
        df_filtered_grouped_counted =  df_in_date_range.groupby(by="production_year").count()\
            .drop(columns=["fin", "production_date", "country", "motor_type"])
        df_filtered_grouped_counted.plot(use_index=True, color="gray", kind="bar")
        plt.title(title)
        plt.legend().set_visible(False)
        plt.xlabel("Year")
        plt.xticks(rotation=0)
        plt.ylabel("Sold Vehicles (pc.)")
        plt.grid(axis="y")
        plt.savefig(self.figure_save_path + "years.png")
        print("________________________________________________________")
        print(title)
        print(df_filtered_grouped_counted)

    def df_fins_sorted_dates(self):
        df_filtered = self.final_table.sort_values(by="production_date").drop(columns=["country", "counter", "motor_type"])
        print("________________________________________________________")
        print("First sold vehicle (FIN):")
        print(df_filtered.iloc[0])

    def df_vehicles_by_motor_types(self, date_lower: str, date_upper: str, motors_list: list):
        title = f"Sold vehicles per engine "\
                f"({pd.to_datetime(date_lower, dayfirst=True).year}-{pd.to_datetime(date_upper, dayfirst=True).year})"
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "motor_type"] in motors_list:
                df_in_date_range.drop(row, inplace=True)
        df_grouped_counted = df_in_date_range.groupby(by="motor_type").count().drop(columns=["fin", "country", "production_date"])
        df_grouped_counted.plot(use_index=True, y=["counter"], kind="bar", color="gray")
        plt.title(title)
        plt.xlabel("Engine type")
        plt.xticks(rotation=0)
        plt.ylabel("Sold Vehicles (pc.)")
        plt.legend().set_visible(False)
        plt.grid(axis="y")
        plt.savefig(self.figure_save_path + "engines.png")
        print("________________________________________________________")
        print(title)
        print(df_grouped_counted)

    def df_vehicles_by_motor_types_country(self, date_lower: str, date_upper: str, motors_list: list, country: str):
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "motor_type"] in motors_list:
                df_in_date_range.drop(row, inplace=True)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "country"] == country:
                df_in_date_range.drop(row, inplace=True)
        print("________________________________________________________")
        print(f"Vehicles (FIN) with engine type {motors_list} and sold to {country} "\
              f"({pd.to_datetime(date_lower, dayfirst=True).year}-{pd.to_datetime(date_upper, dayfirst=True).year})")
        print(df_in_date_range["fin"])
