from pipeline_ex import ETL
from analysis_ex import Analyser

# "database_path": "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler"
# figure_save_path = "C:\\Users\\user\\Dropbox\\DHBW Stuttgart\\Informatik 1 Python\\Projektarbeit_Wiessler\\venv\\vehicle_data_project_exercise\\"

figure_save_path = "\\Users\\jacob\\data\\py\\22-1-04_programming_challenge"
pipeline = ETL("data_specs.json")
final_table = pipeline.run()
analyser = Analyser(final_table, figure_save_path=figure_save_path)
analyser.run()

date_raw = pipeline.raw_data_tables
