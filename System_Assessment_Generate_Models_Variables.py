##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"


#FSA System Assessment
model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
year_original = 2021
version = 103

year_scenario_list = []
year_scenario_list.append([2030,'2030_Network',['Ex']])
year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
year_scenario_list.append([2050,'2030_Network',['2050H']])
year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])

population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File_Update14a15a.xlsx"
population_tab = 'MPF Update 14a'
all_scenarios = True
dual_catchments = False
use_all_files_in_folder = False
output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\Model_Generation'




