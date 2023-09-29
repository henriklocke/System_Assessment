##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"


#FSA System Assessment
model_area = 'FSA'
generate_future = False
generate_bsf = False
generate_xadwf = False
generate_sealed_vfd = False
generate_ad = True

output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\Model_Generation'
script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

#For all models:
version = 105

#For future models
model_original = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\BACKUP\FSA_Base_2021pop_Backup106.sqlite"
# model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
year_original = 2021
year_scenario_list = []
year_scenario_list.append([2021,'Base',['Ex']])
year_scenario_list.append([2030,'2030_Network',['Ex']])
year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
year_scenario_list.append([2050,'2030_Network',['2050H']])
year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File_Update14a15a.xlsx"
population_tab = 'MPF Update 14a'

#For sealed VFD
vfd_all = True
seal_all = True

excluded_asset_names = []
excluded_asset_names.append('Golden Ears SSO Tank')
excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
excluded_asset_names.append('')

weir_turn_offs = []
weir_turn_offs.append('NS4-SSO')

#For BSF
gwis = [11.2]

#For X ADWF
times_adwf_list = [3]

#For AD
dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
model_suffix = '_5y24h_Tracer_WW'
tracer_csv = 'Tracer_Zones.csv'
boundary_tracer_ext = '_t' #added to boundary item id for tracers
sim_ext = "AD_"



