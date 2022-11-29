import datetime

from pipeline_ex import ETL
from analysis_ex import DataFilter, Analyser

# "database_path": "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler"
# figure_save_path = "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler\\venv\\vehicle_data_project_exercise\\"

figure_save_path = "\\Users\\jacob\\data\\py\\22-1-04_programming_challenge"
pipeline = ETL("data_specs.json")
final_table = pipeline.run()
filter_2014_2020 = DataFilter(data_frame=final_table,
                              date_lower="1.1.2014",
                              date_upper="31.12.2014")
data_filter_2014_2020 = filter_2014_2020.for_dates()
"""analyser = Analyser(final_table, figure_save_path=figure_save_path)
analyser.run()"""

