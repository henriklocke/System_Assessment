##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"


#FSA For training
model_area = 'FSA'
generate_future = True
generate_bsf = True
generate_xadwf = False
generate_sealed_vfd = True
generate_ad = False

output_folder = r'J:\TOOLS\Training\Week_58_Create_Multiple_Models\Demo'
script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

#For all models:
version = 127

#For future models
model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
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
inis = [11.2,16.8]

#For X ADWF
times_adwf_list = [3,4]

#For AD
dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
model_suffix = '_5y24h_Tracer_WW'
tracer_csv = 'Tracer_Zones.csv'
boundary_tracer_ext = '_t' #added to boundary item id for tracers
sim_ext = "AD_"
runoff_tracer = False
ww_tracer = True
gwi_tracer = False
include_gwi_in_ww = True
tracer_from_original_zone = False
global_zone_only = True
single_tracer = True
single_tracer_ids = ['All','All']
file_suffix = "_AD"
















# #NSSA BSF
# model_area = 'NSSA'
# generate_future = False
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = True
# generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-BSF\Model_V79_Sealed_VFD'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 79

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\NSSA\01_MASTER_MODEL\MODEL\NSSA_Base.sqlite"
# # model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2018
# year_scenario_list = []
# # year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# year_scenario_list.append([2050,'2030_Network',['2050H']])
# year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# # year_scenario_list.append([2076,'Base',['Ex']])
# population_sheet = r"J:\SEWER_AREA_MODELS\NSSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\NSSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 2'

# #For sealed VFD
# vfd_all = True
# seal_all = True

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# #For BSF
# gwis = [11.2]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA Bypass
# model_area = 'FSA'
# generate_future = True
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Royal_Avenue_Bypass\Model'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 116

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# # model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# # year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2031,'2030_Network',['Ex']])
# # year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# # year_scenario_list.append([2050,'2030_Network',['2050H']])
# # year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File_Update14a15a.xlsx"
# population_tab = 'MPF Update 14a'

# #For sealed VFD
# vfd_all = True
# seal_all = True

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# #For BSF
# gwis = [33.6]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"


# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA BSF
# model_area = 'FSA'
# generate_future = True
# generate_bsf = True
# generate_xadwf = False
# generate_sealed_vfd = True
# generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V126_Sealed_VFD\gen'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 126

# #For future models
# # model_original = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\BACKUP\FSA_Base_2021pop_Backup126.sqlite"
# model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# # year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# year_scenario_list.append([2050,'2030_Network',['2050H']])
# year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File_Update14a15a.xlsx"
# population_tab = 'MPF Update 14a'

# #For sealed VFD
# vfd_all = True
# seal_all = True

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# #For BSF
# # gwis = [11.2,16.8,22.4,25.76,28,33.6]
# gwis = [12.88,15.12,16.24]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# #NSSA System Assessment
# model_area = 'NSSA'
# generate_future = True
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-BSF\SA_Maps_V79\deleteme'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 79

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\NSSA\01_MASTER_MODEL\MODEL\NSSA_Base.sqlite"
# # model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2018
# year_scenario_list = []
# # year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# year_scenario_list.append([2050,'2030_Network',['2050H']])
# year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# # year_scenario_list.append([2076,'Base',['Ex']])
# population_sheet = r"J:\SEWER_AREA_MODELS\NSSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\NSSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 2'

# #For sealed VFD
# vfd_all = True
# seal_all = True

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# #For BSF
# gwis = [11.2]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # #FSA AD
# model_area = 'FSA'
# generate_future = False
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = True

# output_folder = r'\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\FSA_NORTH\03_SIMULATION_WORK\New Sapperton PS and NWI HGLs\Model_AD_Nov2023'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 105

# #For future models

# # model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# year_scenario_list.append([2050,'2030_Network',['2050H']])
# year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File_Update14a15a.xlsx"
# population_tab = 'MPF Update 14a'

# #For sealed VFD
# vfd_all = True
# seal_all = True

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# #For BSF
# gwis = [11.2]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA System Assessment
# model_area = 'FSA'
# generate_future = False
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = True

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\FSA_NORTH\03_SIMULATION_WORK\New Sapperton PS and NWI HGLs\Model_AD_Oct2023'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 114

# #For future models

# # model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# year_scenario_list.append([2050,'2030_Network',['2050H']])
# year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File_Update14a15a.xlsx"
# population_tab = 'MPF Update 14a'

# #For sealed VFD
# vfd_all = True
# seal_all = True

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# #For BSF
# gwis = [11.2]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"




