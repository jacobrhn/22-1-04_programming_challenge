import pandas as pd

class DataFilter:
    def __init__(self, data_frame: pd.DataFrame, date_lower: str = None, date_upper: str = None):
        self.filtered_data = pd.DataFrame(data=data_frame)
        self.__date_lower = pd.to_datetime(date_lower, dayfirst=True)
        self.__date_upper = pd.to_datetime(date_upper, dayfirst=True)

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

    def filter_for_years(self, date_lower: str = None, date_upper: str = None):
        date_lower = pd.to_datetime(date_lower, dayfirst=True)
        date_upper = pd.to_datetime(date_upper, dayfirst=True)
        df = self.final_table
        df["counter"] = 1
        for row in df.index:
            if not date_lower <= df.loc[row, "production_date"] <= date_upper:
                df.drop(row, inplace=True)
        return df.reset_index(drop=True)

    def __df_with_date_range(self, date_lower: str, date_upper: str):
        filtered_data = DataFilter(data_frame=self.final_table, date_lower=date_lower, date_upper=date_upper)
        return filtered_data.for_dates()

    def df_sales_top_three_countries(self, date_lower: str, date_upper: str):
        return self.__df_with_date_range(date_lower=date_lower, date_upper=date_upper) \
            .groupby(by=["country"]).count()\
            .sort_values(by=["fin", "country"], ascending=False)\
            .drop(columns=["fin", "production_date", "motor_type"])\
            .iloc[[0, 1, 2]]

    def df_sales_by_year(self, date_lower: str, date_upper: str):
        df_data_in_date_range = self.__df_with_date_range(date_lower=date_lower, date_upper=date_upper)
        df_data_in_date_range.loc[:, "production_year"] = pd.DatetimeIndex(df_data_in_date_range.loc[:, "production_date"]).year
        return df_data_in_date_range.groupby(by="production_year").count().sort_values(by="counter", ascending=False) \
            .drop(columns=["fin", "production_date", "country", "motor_type"])

    def df_fins_sorted_dates(self):
        return self.final_table.sort_values(by="production_date").drop(columns=["country", "counter", "motor_type"])

    def df_vehicles_by_motor_types(self, date_lower: str, date_upper: str, motors_list: list):
        df_data_in_date_range = self.__df_with_date_range(date_lower=date_lower, date_upper=date_upper)
        for row in df_data_in_date_range.index:
            if not df_data_in_date_range.loc[row, "motor_type"] in motors_list:
                df_data_in_date_range.drop(row, inplace=True)
        return df_data_in_date_range.groupby(by="motor_type").count().drop(columns=["fin", "country", "production_date"])

    def df_vehicles_by_motor_types_country(self, date_lower: str, date_upper: str, motors_list: list, country: str):
        df_data_in_date_range = self.__df_with_date_range(date_lower=date_lower, date_upper=date_upper)
        for row in df_data_in_date_range.index:
            if not df_data_in_date_range.loc[row, "motor_type"] in motors_list:
                df_data_in_date_range.drop(row, inplace=True)
        for row in df_data_in_date_range.index:
            if not df_data_in_date_range.loc[row, "country"] == country:
                df_data_in_date_range.drop(row, inplace=True)
        return df_data_in_date_range["fin"]



    def visualize_sales_per_countries(self):
        # your code here #
        pass

    def visualize_sales_per_year(self):
        # your code here #
        pass
