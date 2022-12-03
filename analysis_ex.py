import pandas
import pandas as pd
import matplotlib.pyplot as plt


class Analyser:
    def __init__(self, table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table

    @staticmethod
    def text_output(description: str, data, filepath=None):
        print("________________________________________________")
        print(description)
        print(data)
        if filepath:
            print(f"Figure saved to {filepath}")

    @staticmethod
    def __create_fig(data_y_axis, figure_save_path, title: str, label_x_axis: str, label_y_axis: str, color: str,
                    figure_kind: str,
                    file_suffix: str, data: pandas.DataFrame, ):
        data.plot(use_index=True, y=[data_y_axis], kind=figure_kind, color=color)
        plt.title(title)
        plt.legend().set_visible(False)
        plt.xlabel(label_x_axis)
        plt.xticks(rotation=0)
        plt.ylabel(label_y_axis)
        plt.grid(axis="y")
        plt.savefig(figure_save_path + "_" +file_suffix)

    def filter_for_years(self, date_lower: str = None, date_upper: str = None):
        date_lower = pd.to_datetime(date_lower, dayfirst=True)
        date_upper = pd.to_datetime(date_upper, dayfirst=True)
        df_in_date_range = self.final_table
        for row in df_in_date_range.index:
            if not pd.to_datetime(date_lower, dayfirst=True) \
                   <= df_in_date_range.loc[row, "production_date"] <= pd.to_datetime(date_upper, dayfirst=True):
                df_in_date_range.drop(row, inplace=True)
        return df_in_date_range.reset_index(drop=True)

    def df_sales_top_three_countries(self, date_lower: str, date_upper: str):
        str_date_range = f"{pd.to_datetime(date_lower, dayfirst=True).year}_{pd.to_datetime(date_upper, dayfirst=True).year}"
        description = f"Top Three: sold vehicles per country ({str_date_range})"
        df_filtered_grouped_counted = self.filter_for_years(date_lower=date_lower, date_upper=date_upper) \
            .groupby(by=["country"]).count() \
            .sort_values(by=["fin", "country"], ascending=False) \
            .drop(columns=["fin", "production_date", "motor_type"]) \
            .iloc[[0, 1, 2]]
        self.__create_fig(data_y_axis="counter", figure_save_path=self.figure_save_path, title=description,
                          label_x_axis="Country", label_y_axis="Sold Vehicles (pc.)", color="gray", figure_kind="bar",
                          file_suffix=f"by_country_{str_date_range}",
                          data=df_filtered_grouped_counted)
        self.text_output(description=description, data=df_filtered_grouped_counted, filepath=self.figure_save_path)

    def df_sales_by_year(self, date_lower: str, date_upper: str):
        str_date_range = f"{pd.to_datetime(date_lower, dayfirst=True).year}_{pd.to_datetime(date_upper, dayfirst=True).year}"
        description = f"Sold vehicles per year ({str_date_range})"
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        df_in_date_range.loc[:, "production_year"] = pd.DatetimeIndex(df_in_date_range.loc[:, "production_date"]).year
        df_filtered_grouped_counted = df_in_date_range.groupby(by="production_year").count() \
            .drop(columns=["fin", "production_date", "country", "motor_type"])
        self.__create_fig(data_y_axis="counter", figure_save_path=self.figure_save_path, title=description,
                          label_x_axis="Year", label_y_axis="Sold Vehicles (pc.)", color="gray", figure_kind="bar",
                          file_suffix=f"pc_per_year_{str_date_range}", data=df_filtered_grouped_counted)
        self.text_output(description=description, data=df_filtered_grouped_counted, filepath=self.figure_save_path)

    def df_fins_sorted_dates(self):
        df_filtered = self.final_table.sort_values(by="production_date").drop(
            columns=["country", "counter", "motor_type"])
        self.text_output(description="First sold vehicle (FIN):", data=df_filtered.iloc[0])

    def df_vehicles_by_motor_types(self, date_lower: str, date_upper: str, motors_list: list):
        str_date_range = f"{pd.to_datetime(date_lower, dayfirst=True).year}_{pd.to_datetime(date_upper, dayfirst=True).year}"
        description = f"Sold vehicles per engine ({str_date_range})"
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "motor_type"] in motors_list:
                df_in_date_range.drop(row, inplace=True)
        df_filtered_grouped_counted = df_in_date_range.groupby(by="motor_type").count().drop(
            columns=["fin", "country", "production_date"])
        self.__create_fig(data_y_axis="counter", figure_save_path=self.figure_save_path, title=description,
                          label_x_axis="Engine type", label_y_axis="Sold Vehicles (pc.)", color="gray", figure_kind="bar",
                          file_suffix=f"engines_{str_date_range}", data=df_filtered_grouped_counted)
        self.text_output(description=description, data=df_filtered_grouped_counted, filepath=self.figure_save_path)

    def df_vehicles_by_motor_types_country(self, date_lower: str, date_upper: str, motors_list: list, country: str):
        str_date_range = f"{pd.to_datetime(date_lower, dayfirst=True).year}_{pd.to_datetime(date_upper, dayfirst=True).year}"
        df_in_date_range = self.filter_for_years(date_lower=date_lower, date_upper=date_upper)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "motor_type"] in motors_list:
                df_in_date_range.drop(row, inplace=True)
        for row in df_in_date_range.index:
            if not df_in_date_range.loc[row, "country"] == country:
                df_in_date_range.drop(row, inplace=True)
        self.text_output(description=f"Vehicles (FIN) with engine type {motors_list} and sold to {country} "
                                     f"({str_date_range})", data=df_in_date_range["fin"])
