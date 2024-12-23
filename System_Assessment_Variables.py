##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"

#Defaults
sum_positive_only = False
skip_first_day = True



##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# #VSA Test
# model_area = "VSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0002
# sum_positive_only = False

# result_specs_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\86. Copley San Sewer Assessment\Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\86. Copley San Sewer Assessment\Maps\Import_Specs\PS_Capacity_VSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\86. Copley San Sewer Assessment\Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\86. Copley San Sewer Assessment\Maps\Import_Specs\Summation_PS_Short.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\86. Copley San Sewer Assessment\Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\86. Copley San Sewer Assessment\Maps3"
# result_folder = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\86. Copley San Sewer Assessment\Model3" #model folder


# ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# #FSA Always latest
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\Model"

# ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# #FSA Annacis
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Annacis_2019-2024\SA_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Annacis_2019-2024\Model"

# ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# #VSA Test
# model_area = "VSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0002
# sum_positive_only = True

# result_specs_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Design_Storms_Test_Positive\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Design_Storms_Test_Positive\Import_Specs\PS_Capacity_VSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Design_Storms_Test_Positive\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Design_Storms_Test_Positive\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Design_Storms_Test_Positive\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Design_Storms_Test_Positive"
# result_folder = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\78. Comparison of Columbia PS Operating Strategies\HD Results (5 Year Design Storm)"

# ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# #FSA cal
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\BLNI2_In_Line_Storage\SA_MAPS_GATE_SPLIT\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2024\SA_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2024\DWF_Calibration_Full_Package\Model"


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # # FSA X BSF VFD
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1_OBS\SA_Maps_V147_Sealed_VFD\Import_Specs\Result_Specifications.csv"
# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_3\SA_Maps_V152_Sealed_VFD_Upsize_RX_Ann0p8\PS_Capacity_FSA_2030_Network.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1_OBS\SA_Maps_V147_Sealed_VFD\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1_OBS\SA_Maps_V147_Sealed_VFD\Import_Specs\Summation_PS.csv"
# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1_OBS\SA_Maps_V147_Sealed_VFD\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Maps_V183_Ann0p8_UpsNSIRX_0p3cms"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V183_Ann0p8_UpsNSIRX_0p3cms"

# # FSA X BSF VFD
model_area = "FSA"

set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1_OBS\SA_Maps_V147_Sealed_VFD\Import_Specs\Result_Specifications.csv"
ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_3\SA_Maps_V152_Sealed_VFD_Upsize_RX_Ann0p8\PS_Capacity_FSA_2030_Network.csv"
summation_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1_OBS\SA_Maps_V147_Sealed_VFD\Import_Specs\Summation.csv"
summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1_OBS\SA_Maps_V147_Sealed_VFD\Import_Specs\Summation_PS.csv"
outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1_OBS\SA_Maps_V147_Sealed_VFD\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\SA_Maps_V187_Ann0p8_0p3cms"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_0\Model_V187_Ann0p8_0p3cms"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Maps_V187_Ann0p8_UpsNSIRX1p2m(A)_0p3cms"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSIRX1p2m(A)_0p3cms"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Maps_V187_Ann0p8_UpsNSIRX2m(B)_0p3cms"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSIRX2m(B)_0p3cms"

map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Maps_V187_Ann0p8_UpsNSR(C)_0p3cms"
result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\EFLSP_Modelling\Phase_1\Model_V187_Ann0p8_UpsNSR(C)_0p3cms"

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # FSA X BSF Sealed VFD
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\SA_Maps_V147_Sealed_VFD\Import_Specs\Result_Specifications.csv"
# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\SA_Maps_V147_Sealed_VFD\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\SA_Maps_V147_Sealed_VFD\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\SA_Maps_V147_Sealed_VFD\Import_Specs\Summation_PS.csv"
# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\SA_Maps_V147_Sealed_VFD\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\SA_Maps_V147_Sealed_VFD_AIWWT_17cms"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\X_Times_BSF\Model_V147_Sealed_VFD_AIWWTP_17cms"



##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA Cal
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Cloverdale_2030_Network_Test\SA_Maps\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_FSA\SA_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\NW_CSO_Tank_Disabled_Test\SA_Maps"
# result_folder = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\NW_CSO_Tank_Disabled_Test\Model"



##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA System Assessment Sealed VFD
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\Design\Event_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment_All_Sealed_VFD"


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA System Assessment
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment"

# ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



# # #NSSA always latest
# model_area = "NSSA"
# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001
# result_specs_csv = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\SA_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\SA_Maps\Import_Specs\PS_Capacity_NSSA.csv"
# summation_csv = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\SA_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\SA_Maps\Import_Specs\Summation_PS.csv"
# outfall_csv = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\SA_Maps\Import_Specs\Outfall_Summary.csv"
# map_folder = r"\\prdsynfile01\LWS_Modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\SA_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Always_Latest_Master_Model_Simulations_NSSA\Model"



##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA System Assessment
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment"


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA MIKE+ review
# model_area = "FSA"
# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001
# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023p1_September_2023\SA_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023p1_September_2023\SA_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023p1_September_2023\SA_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023p1_September_2023\SA_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023p1_September_2023\SA_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\MU_Classic_To_MIKE+_Sim_Compare\MIKEPLUS_2023p1_September_2023\SA_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\01_MASTER_MODEL\MODEL\FSA_Base_2021pop_m1d - Result Files"



##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # #NSSA X BSF
# model_area = "NSSA"
# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001
# result_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\PS_Capacity_NSSA.csv"
# summation_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Summation_PS.csv"
# outfall_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Outfall_Summary.csv"
# map_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-BSF\SA_Maps_V86_Sealed_VFD"
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-BSF\Model_V86_Sealed_VFD"


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # #NSSA Hollyburn flood trial
# model_area = "NSSA"
# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001
# result_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\PS_Capacity_NSSA.csv"
# summation_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Hollyburn_Headloss_trial\SA_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\Hollyburn_Headloss_trial\Model\NSSA_Base_m1d - Result Files"

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Golden Ears Tank
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\Golden Ears SSO Tank Optimization\Review_Henrik\SA_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\Golden Ears SSO Tank Optimization\Review_Henrik\Models_Results"

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA System Assessment Sealed VFD
# model_area = "FSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001

# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Event_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\Design\Event_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment\FSA_System_Assessment_All_Sealed_VFD"



##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # #NSSA System Assessment Sealed VFD
# model_area = "NSSA"
# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001
# result_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\PS_Capacity_NSSA.csv"
# summation_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\Design\Event_Maps"
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\NSSA_SYSTEM_ASSESSMENT_ALL_BOLTED_VFD"

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # #NSSA System Assessment
# model_area = "NSSA"
# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001
# result_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\PS_Capacity_NSSA.csv"
# summation_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Summation.csv"
# summation_ps_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Summation_PS.csv"

# outfall_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps\Import_Specs\Outfall_Summary.csv"

# map_folder = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_mapping\NSSA_Event_Maps"
# result_folder = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\SYSTEM_ASSESSMENT\NSSA_SYSTEM_ASSESSMENT"


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA Port Moody BSF
# model_area = "FSA"
# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001
# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Sealed_VFD_Version50\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Sealed_VFD_Version50\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Sealed_VFD_Version50\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Sealed_VFD_Version50\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Sealed_VFD_Version50\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Sealed_VFD_Version50"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\System_Assessment_Special_Runs\Sealed_VFD_Version50"

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #FSA Port Moody BSF
# model_area = "FSA"
# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0001
# result_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Port_Moody_BSF\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Port_Moody_BSF\Import_Specs\PS_Capacity_FSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Port_Moody_BSF\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Port_Moody_BSF\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Port_Moody_BSF\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Port_Moody_BSF"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_Custom_Maps\Custom_Event_Maps\Port_Moody_BSF"



##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# model_area = "VSA"

# set_pipe_volume_0_when_max_pipe_flow_less_than_cms = 0.0003

# result_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_DWF\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_DWF\Import_Specs\PS_Capacity_VSA.csv"
# summation_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_DWF\Import_Specs\Summation.csv"
# summation_ps_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_DWF\Import_Specs\Summation_PS.csv"

# outfall_csv = r"\\prdsynfile01\lws_modelling\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_DWF\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\DWF_No_Tide\RESULTS\Debug"
# result_folder = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\DWF_No_Tide\RESULTS\Debug"


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#VSA
# result_specs_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Test_Jupyter\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Test_Jupyter\Import_Specs\PS_Capacity_VSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Test_Jupyter\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Test_Jupyter\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Test_Jupyter\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\VSA_Event_Maps_Test_Jupyter"
# result_folder = r"J:\SEWER_AREA_MODELS\VSA\04_ANALYSIS_WORK\21. SYSTEM_ASSESSMENT\Design Storms\MODEL"

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# model_area = "NSSA"

# result_specs_csv = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\SA_Maps_External_Standard\Import_Specs\Result_Specifications.csv"

# ps_specs_csv = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\SA_Maps_External_Standard\Import_Specs\PS_Capacity_NSSA.csv"
# summation_csv = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\SA_Maps_External_Standard\Import_Specs\Summation.csv"
# summation_ps_csv = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\SA_Maps_External_Standard\Import_Specs\Summation_PS.csv"

# outfall_csv = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\SA_Maps_External_Standard\Import_Specs\Outfall_Summary.csv"

# map_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\SA_Maps_External_Standard"
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model"