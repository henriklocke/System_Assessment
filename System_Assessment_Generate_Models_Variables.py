##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"




#FSA For misc stuff
model_area = 'FSA'
generate_future = True
generate_bsf = True
generate_xadwf = False
generate_sealed_vfd = True
generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_V185_Ann0p8_0p3cms\gen' #Create a 
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V184_Ann0p8_UpsNSIRX1p2m(A)_0p3cms\gen'

##0
model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_V187_Ann0p8_0p3cms\Original\FSA_Base_2021pop_V187_Ann0p8_NSI0p3cms.sqlite"
output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_V187_Ann0p8_0p3cms\Gen'


#1A
# model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSIRX1p2m(A)_0p3cms\Original\FSA_Base_2021pop_V187_Ann0p8_NSI0p3cms_1A.sqlite"
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSIRX1p2m(A)_0p3cms\gen'

# # 1B
# model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSIRX2m(B)_0p3cms\Original\FSA_Base_2021pop_V187_Ann0p8_NSI0p3cms.sqlite"
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSIRX2m(B)_0p3cms\gen'


# #1C
# model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSR(C)_0p3cms\Original\FSA_Base_2021pop_V187_Ann0p8_NSI0p3cms.sqlite"
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSR(C)_0p3cms\Gen'

# output_folder = r''

# folder and this is your model folder
script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

#For all models:
version = 187

#For future models
# model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_V185_Ann0p8_0p3cms\Original\FSA_Base_2021pop_V185_Ann0p8_NSI0p3cms.sqlite" #DO USE THE SQLITE
# model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V184_Ann0p8_UpsNSIRX1p2m(A)_0p3cms\Original\FSA_Base_2021pop_V184_Ann0p8_NSI0p3cms.sqlite"

# model_original = r


year_original = 2021 #the pop year in the row entitled "model_original" should match the pop year in this row
year_scenario_list = []
# year_scenario_list.append([2023,'Base',['Ex']])
year_scenario_list.append([2030,'2030_Network',['Ex']])
year_scenario_list.append([2035,'2030_Network',['Ex']])
year_scenario_list.append([2040,'2030_Network',['2050M','2050H']]) # The 2050M etc enables the batch run in the simulation setup
year_scenario_list.append([2045,'2030_Network',['2050M','2050H']])
year_scenario_list.append([2050,'2030_Network',['2050M','2050H']])
# # year_scenario_list.append([2055,'2030_Network',['2050M','2050H']])
year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# # year_scenario_list.append([2065,'2030_Network',['2050H','2100H']])
# # year_scenario_list.append([2070,'2030_Network',['2050M','2050H']])
year_scenario_list.append([2075,'2030_Network',['2050M','2050H']])
# # year_scenario_list.append([2080,'2030_Network',['2050H','2100H']])
year_scenario_list.append([2090,'2030_Network',['2050H','2100H']])
year_scenario_list.append([2100,'2030_Network',['2050H','2100H']])
population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
population_tab = 'MPF Update 17'

#For sealed VFD
vfd_all = True
seal_all = True
custom_sqls = []

excluded_asset_names = []
excluded_asset_names.append('Golden Ears SSO Tank')
excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
excluded_asset_names.append('')

weir_turn_offs = []
weir_turn_offs.append('NS4-SSO')

#For BSF
# inis = [14.56,15.12]
inis = [11.2,12.88,14,14.56,15.12,15.68,16.8]

# inis = [11.2,11.76,12.32,12.88,13.44,14,14.56,15.12,15.68,16.8]
# inis = [11.2,11.76,12.32,12.88,13.44,14]
# inis = [11.2,12.88,14]
# inis = [14.56,15.12,15.68,16.8]

sim_start_date = '2020-01-29'
sim_end_date = '2020-02-02'


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

# ################################################################################################################


# #FSA For misc stuff
# model_area = 'FSA'
# generate_future = True
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = False



# # output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_V185_Ann0p8_0p3cms\gen' #Create a 
# # output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V184_Ann0p8_UpsNSIRX1p2m(A)_0p3cms\gen'
# output_folder = r'\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\REQUESTS\Joshua Redmond_NWW_NWX_New West_Laterals_Analysis\Stage 4_12182024\Model\Gen'
# # output_folder = r''

# # folder and this is your model folder
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 185

# #For future models
# # model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_V185_Ann0p8_0p3cms\Original\FSA_Base_2021pop_V185_Ann0p8_NSI0p3cms.sqlite" #DO USE THE SQLITE
# # model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V184_Ann0p8_UpsNSIRX1p2m(A)_0p3cms\Original\FSA_Base_2021pop_V184_Ann0p8_NSI0p3cms.sqlite"
# model_original = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\REQUESTS\Joshua Redmond_NWW_NWX_New West_Laterals_Analysis\Stage 4_12182024\Model\FSA_Base_2021pop_V185_NWX_1Barrel.sqlite"
# # model_original = r


# year_original = 2021 #the pop year in the row entitled "model_original" should match the pop year in this row
# year_scenario_list = []
# # year_scenario_list.append([2023,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# # year_scenario_list.append([2035,'2030_Network',['Ex']])
# # year_scenario_list.append([2040,'2030_Network',['2050M','2050H']]) # The 2050M etc enables the batch run in the simulation setup
# # year_scenario_list.append([2045,'2030_Network',['2050M','2050H']])
# # year_scenario_list.append([2050,'2030_Network',['2050M','2050H']])
# # # # year_scenario_list.append([2055,'2030_Network',['2050M','2050H']])
# # year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# # # # year_scenario_list.append([2065,'2030_Network',['2050H','2100H']])
# # # # year_scenario_list.append([2070,'2030_Network',['2050M','2050H']])
# # year_scenario_list.append([2075,'2030_Network',['2050M','2050H']])
# # # # year_scenario_list.append([2080,'2030_Network',['2050H','2100H']])
# # year_scenario_list.append([2090,'2030_Network',['2050H','2100H']])
# # year_scenario_list.append([2100,'2030_Network',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 17'


# #For sealed VFD
# vfd_all = True
# seal_all = True
# custom_sqls = []

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# #For BSF
# # inis = [14.56,15.12]
# inis = [11.2,11.76,12.32,12.88,13.44,14,14.56,15.12,15.68,16.8]

# # inis = [11.2,11.76,12.32,12.88,13.44,14,14.56,15.12,15.68,16.8]
# # inis = [11.2,11.76,12.32,12.88,13.44,14]
# # inis = [11.2,12.88,14]
# # inis = [14.56,15.12,15.68,16.8]

# sim_start_date = '2020-01-29'
# sim_end_date = '2020-02-02'


# #For X ADWF
# times_adwf_list = [3,4]

# #For AD
# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"
# runoff_tracer = False
# ww_tracer = True
# gwi_tracer = False
# include_gwi_in_ww = True
# tracer_from_original_zone = False
# global_zone_only = True
# single_tracer = True
# single_tracer_ids = ['All','All']
# file_suffix = "_AD"

###############################################################################################################



# #FSA Joshua
# model_area = 'FSA'
# generate_future = True
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = False

# output_folder = r'\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\REQUESTS\Joshua Redmond_ SYC2_HGL Modelling\Model_Joshua\gen'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 147

# #For future models
# model_original = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\BACKUP\FSA_Base_2021pop_Backup147.sqlite"
# model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# # year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2030,'Base',['Ex']])

# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\Master Population Update Files\FSA_Population_Update_016.xlsx"
# population_tab = 'MPF Update 16'

# #For sealed VFD
# vfd_all = True
# seal_all = False

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# custom_sqls = []

# #For BSF
# # inis = [11.2,14,14.56,15.68,16.24,16.8]
# # inis = [11.2,12.88,14,15.12,16.24,16.8,22.4,25.76,28,33.6]
# #inis = [22.4]
# sim_start_date = '2020-01-29'
# sim_end_date = '2020-02-02'
# inis = [11.2,22.4,33.6,44.8]


# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"


################################################################################################################



# #FSA LTS
# model_area = 'FSA'
# generate_future = True
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = False

# # output_folder = r'C:\Users\hloecke\Desktop\faster\Test'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\LTS\Model_2023-4'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 157

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# year_scenario_list.append([2023,'Base',['Ex']])
# # year_scenario_list.append([2030,'2030_Network',['Ex']])
# # year_scenario_list.append([2040,'Base',['2050M','2050H']])
# # year_scenario_list.append([2060,'Base',['2050H','2100H']])
# # year_scenario_list.append([2080,'Base',['2050H','2100H']])
# # year_scenario_list.append([2100,'Base',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 17'

# #For sealed VFD
# vfd_all = True
# seal_all = False

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# custom_sqls = []
# # custom_sqls.append("UPDATE msm_Orifice SET enabled = 0 WHERE muid = 'LynnSiphonBlowDownOrifice'")
# # custom_sqls.append("UPDATE msm_RTC SET enabled = 0 WHERE muid = '8_LynnSiphonBlowDownOrifice'")

# #For BSF
# #Dates format must be formatted like '2020-01-29'
# sim_start_date = '2020-01-29'
# sim_end_date = '2020-02-02'
# inis = [11.2]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = ""
# wastewater_only = True
# model_suffix = '_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"
# runoff_tracer = False
# ww_tracer = True
# gwi_tracer = False
# include_gwi_in_ww = True
# tracer_from_original_zone = False
# global_zone_only = True
# single_tracer = True
# single_tracer_ids = ['All','All']
# file_suffix = "_AD"


################################################################################################################


# #FSA GIS input
# model_area = 'FSA'
# generate_future = True
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = False

# # output_folder = r'C:\Users\hloecke\Desktop\faster\Test'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_FSA\Model'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 183

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# year_scenario_list.append([2025,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# # year_scenario_list.append([2040,'Base',['2050M','2050H']])
# # year_scenario_list.append([2060,'Base',['2050H','2100H']])
# # year_scenario_list.append([2080,'Base',['2050H','2100H']])
# # year_scenario_list.append([2100,'Base',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 17'

# #For sealed VFD
# vfd_all = True
# seal_all = False

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# custom_sqls = []
# # custom_sqls.append("UPDATE msm_Orifice SET enabled = 0 WHERE muid = 'LynnSiphonBlowDownOrifice'")
# # custom_sqls.append("UPDATE msm_RTC SET enabled = 0 WHERE muid = '8_LynnSiphonBlowDownOrifice'")

# #For BSF
# #Dates format must be formatted like '2020-01-29'
# sim_start_date = '2020-01-29'
# sim_end_date = '2020-02-02'
# inis = [11.2]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = ""
# wastewater_only = True
# model_suffix = '_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"
# runoff_tracer = False
# ww_tracer = True
# gwi_tracer = False
# include_gwi_in_ww = True
# tracer_from_original_zone = False
# global_zone_only = True
# single_tracer = True
# single_tracer_ids = ['All','All']
# file_suffix = "_AD"


# ################################################################################################################


# #Westridge AD
# model_area = 'FSA'
# generate_future = True
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = False

# # output_folder = r'C:\Users\hloecke\Desktop\faster\Test'
# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Westridge_AD_Modeling\Model\Gen'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 151

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Westridge_AD_Modeling\Model\FSA_Base_2021pop_V140_Step3_Simple_BBY.sqlite"
# year_original = 2021
# year_scenario_list = []
# year_scenario_list.append([2023,'Base',['Ex']])
# # year_scenario_list.append([2030,'2030_Network',['Ex']])
# # year_scenario_list.append([2040,'Base',['2050M','2050H']])
# # year_scenario_list.append([2060,'Base',['2050H','2100H']])
# # year_scenario_list.append([2080,'Base',['2050H','2100H']])
# # year_scenario_list.append([2100,'Base',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 17'

# #For sealed VFD
# vfd_all = True
# seal_all = False

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# custom_sqls = []
# # custom_sqls.append("UPDATE msm_Orifice SET enabled = 0 WHERE muid = 'LynnSiphonBlowDownOrifice'")
# # custom_sqls.append("UPDATE msm_RTC SET enabled = 0 WHERE muid = '8_LynnSiphonBlowDownOrifice'")

# #For BSF
# #Dates format must be formatted like '2020-01-29'
# sim_start_date = '2020-01-29'
# sim_end_date = '2020-02-02'
# inis = [11.2]

# #For X ADWF
# times_adwf_list = [3]

# #For AD
# dfs0_file = ""
# wastewater_only = True
# model_suffix = '_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"
# runoff_tracer = False
# ww_tracer = True
# gwi_tracer = False
# include_gwi_in_ww = True
# tracer_from_original_zone = False
# global_zone_only = True
# single_tracer = True
# single_tracer_ids = ['All','All']
# file_suffix = "_AD"


# ################################################################################################################
# #NSSA for special case
# model_area = 'NSSA'
# generate_future = False
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = True
# generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\GE_2076_Design_Flows_Dry_Wet_Rerun_V86\Model'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 89

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\NSSA\01_MASTER_MODEL\MODEL\NSSA_Base_2018pop.sqlite"
# year_original = 2018
# year_scenario_list = []
# year_scenario_list.append([2076,'Base',['Ex']])
# population_sheet =r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\GE_2076_Design_Flows_Dry_Wet_Rerun_V86\NSSA_Master_Population_X_Remake_Special_GE_2076.xlsx'
# population_tab = 'MPF Update X'

# #For sealed VFD
# vfd_all = True
# seal_all = False

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# custom_sqls = []
# # custom_sqls.append("UPDATE msm_Orifice SET enabled = 0 WHERE muid = 'LynnSiphonBlowDownOrifice'")
# # custom_sqls.append("UPDATE msm_RTC SET enabled = 0 WHERE muid = '8_LynnSiphonBlowDownOrifice'")

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

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# #NSSA for GIS input
# model_area = 'NSSA'
# generate_future = True
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = False
# generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Key_Flow_HGL_GIS_Sim_NSSA\Model'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 93

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\NSSA\01_MASTER_MODEL\MODEL\NSSA_Base_2023pop.sqlite"
# year_original = 2023
# year_scenario_list = []
# year_scenario_list.append([2025,'Base',['Ex']])
# year_scenario_list.append([2030,'Base',['Ex']])
# population_sheet = r"J:\SEWER_AREA_MODELS\NSSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\NSSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 4'

# #For sealed VFD
# vfd_all = True
# seal_all = True

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# custom_sqls = []
# # custom_sqls.append("UPDATE msm_Orifice SET enabled = 0 WHERE muid = 'LynnSiphonBlowDownOrifice'")
# # custom_sqls.append("UPDATE msm_RTC SET enabled = 0 WHERE muid = '8_LynnSiphonBlowDownOrifice'")

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

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# #FSA For misc stuff
# model_area = 'FSA'
# generate_future = False
# generate_bsf = False
# generate_xadwf = False
# generate_sealed_vfd = True
# generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Headloss Test\MODEL_n_0p013_Conc_Normal_Henrik'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 149

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_3\Model_V149_Sealed_VFD_AIWWTP_17cms_ChangeDate\Template\FSA_Base_2021pop_Ann17.sqlite"
# year_original = 2021
# year_scenario_list = []
# # year_scenario_list.append([2024,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# # year_scenario_list.append([2040,'Base',['2050M','2050H']])
# # year_scenario_list.append([2060,'Base',['2050H','2100H']])
# # year_scenario_list.append([2080,'Base',['2050H','2100H']])
# # year_scenario_list.append([2100,'Base',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 16'


# #For sealed VFD
# vfd_all = True
# seal_all = True
# custom_sqls = []

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# #For BSF
# inis = [11.2,16.8]
# # inis = [28,33.6]


# #For X ADWF
# times_adwf_list = [3,4]

# #For AD

# boundary_tracer_ext = '_t' #added to boundary item id for tracers
# sim_ext = "AD_"
# file_suffix = "_AD"

# wastewater_only = True #If True, ignore all variables below. No new zones will be made.


# dfs0_file = "NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.dfs0"
# model_suffix = '_5y24h_Tracer_WW'
# tracer_csv = 'Tracer_Zones.csv'
# runoff_tracer = False
# ww_tracer = True
# gwi_tracer = False
# include_gwi_in_ww = False
# tracer_from_original_zone = False
# global_zone_only = True
# single_tracer = True
# single_tracer_ids = ['All','All']






# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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

# custom_sqls = []
# custom_sqls.append("UPDATE msm_Orifice SET enabled = 0 WHERE muid = 'LynnSiphonBlowDownOrifice'")
# custom_sqls.append("UPDATE msm_RTC SET enabled = 0 WHERE muid = '8_LynnSiphonBlowDownOrifice'")

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
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 16'

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

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_Master_V164_V\gen'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 164

# #For future models
# # model_original = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\BACKUP\FSA_Base_2021pop_Backup126.sqlite"
# model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# # year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# # year_scenario_list.append([2035,'2030_Network',['Ex']])
# year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# year_scenario_list.append([2050,'2030_Network',['2050H']])
# year_scenario_list.append([2060,'2030_Network',['2050H']])
# year_scenario_list.append([2070,'2030_Network',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 17'

# #For sealed VFD
# vfd_all = True
# seal_all = False

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# custom_sqls = []

# #For BSF
# # inis = [11.2,14,14.56,15.68,16.24,16.8]
# # inis = [11.2,12.88,14,15.12,16.24,16.8,22.4,25.76,28,33.6]
# #inis = [22.4]
# sim_start_date = '2020-01-29'
# sim_end_date = '2020-02-02'
# inis = [11.2,22.4,33.6,44.8]


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
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 16'

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
# generate_future = True
# generate_bsf = True
# generate_xadwf = False
# generate_sealed_vfd = True
# generate_ad = False

# output_folder = r'J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\Model_Generation'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 131

# #For future models

# model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2021
# year_scenario_list = []
# year_scenario_list.append([2021,'Base',['Ex']])
# year_scenario_list.append([2030,'2030_Network',['Ex']])
# year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# year_scenario_list.append([2050,'2030_Network',['2050H']])
# year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# population_sheet = r"J:\SEWER_AREA_MODELS\FSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\FSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 16'

#For sealed VFD
# vfd_all = True
# seal_all = True

# excluded_asset_names = []
# excluded_asset_names.append('Golden Ears SSO Tank')
# excluded_asset_names.append('NW CSO Tank Cleanout Pumps')
# excluded_asset_names.append('')

# weir_turn_offs = []
# weir_turn_offs.append('NS4-SSO')

# inis = [11.2]

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

# output_folder = r'J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\LTS\Model_2021-22'
# script_path = r"J:\TOOLS\Generate_WaterspillDischarge_C#\WaterspillDischarge.cs"

# #For all models:
# version = 86

# #For future models
# model_original = r"J:\SEWER_AREA_MODELS\NSSA\01_MASTER_MODEL\MODEL\NSSA_Base.sqlite"
# # model_original = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop.sqlite"
# year_original = 2018
# year_scenario_list = []
# year_scenario_list.append([2021,'Base',['Ex']])
# # year_scenario_list.append([2030,'2030_Network',['Ex']])
# # year_scenario_list.append([2040,'2030_Network',['2050M','2050H']])
# # year_scenario_list.append([2050,'2030_Network',['2050H']])
# # year_scenario_list.append([2060,'2030_Network',['2050H','2100H']])
# # year_scenario_list.append([2076,'Base',['Ex']])
# population_sheet = r"J:\SEWER_AREA_MODELS\NSSA\02_MODEL_COMPONENTS\04_DATA\01. POPULATION\NSSA_Master_Population_File.xlsx"
# population_tab = 'MPF Update 3'

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




