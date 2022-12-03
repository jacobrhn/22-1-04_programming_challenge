from pipeline_ex import ETL
from analysis_ex import Analyser

# "database_path": "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler"
# figure_save_path = "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler\\venv\\vehicle_data_project_exercise\\"

figure_save_path = "\\Users\\jacob\\filterd_data\\py\\22-1-04_programming_challenge"
pipeline = ETL("data_specs.json")
final_table = pipeline.run()
analyser = Analyser(table=final_table, figure_save_path=figure_save_path)
analyser.df_sales_top_three_countries(date_lower="1.1.2014", date_upper="31.12.2020")
analyser.df_sales_by_year(date_lower="1.1.2014", date_upper="31.12.2020")
analyser.df_fins_sorted_dates()
analyser.df_vehicles_by_motor_types(date_lower="1.1.2017", date_upper="1.1.2021", motors_list=["OM 934", "OM 936", "OM 470", "OM 471"])
analyser.df_vehicles_by_motor_types_country(date_lower="1.1.2017", date_upper="1.1.2021", motors_list=["OM 936"], country="Neuseeland")