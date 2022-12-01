import datetime
from pipeline_ex import ETL
from analysis_ex import DataFilter, Analyser

# "database_path": "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler"
# figure_save_path = "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler\\venv\\vehicle_data_project_exercise\\"

figure_save_path = "\\Users\\jacob\\filterd_data\\py\\22-1-04_programming_challenge"
pipeline = ETL("data_specs.json")
final_table = pipeline.run()
analyser = Analyser(table=final_table, figure_save_path=figure_save_path)
analyser.run()

print(f"\n--- final table ---")
print(final_table)

# print(final_table["sales_code_array"].iloc[0][0:3])
# print(pipeline.raw_data_tables["sales_codes"]["sales_code_array"][0][0:3])

print(final_table)
print(f"\n--- top 3 countries (2014-2020) ---")
print(analyser.df_sales_top_three_countries(date_lower="1.1.2014", date_upper="31.12.2020"))
print(f"\n--- top country (2014-2020) ---")
print(analyser.df_sales_top_country(date_lower="1.1.2014", date_upper="31.12.2020"))

print(analyser.df_first_fin())