

contributor = ('LXZ','FYW',)
# TODO: ORM?

CalTypeKey = 'calculate_type' # LF, ST, SST_LIN, SST_EIG
GetTypeKey = 'get_type' # settings, results
EleTypeKey = 'element_type' # Bus, Tranformer, etc.
EleAttrNameKey = 'attribute_name' # Pg, Qg, etc.
EleIdKey = 'element_id'
EleAttrValueKey = 'attribute_value'

KeyInsertTimeStamp = 'insert_time'
EXE_LF = 'WMLFRTMsg.exe'
EXE_ST = 'wmudrt.exe'
EXE_SST_LIN = 'Wsstlin.exe'
EXE_SST_EIG = 'Wssteig.exe'
WINDOW_NAME_ST = 'Transient Stability Calculation'
FILE_STOUT = 'STOUT.INF'
FILE_TEMPLATE_OUTPUT_ST = 'FN{}.DAT'
PATTERN_OUTPUT_ST = FILE_TEMPLATE_OUTPUT_ST.format(r'\d+')
FILE_PREFIX_LF = 'LF.'
PATTERN_SETTINGS_LF = FILE_PREFIX_LF+'.N{0,1}L\d+'
PATTERN_RESULTS_LF = FILE_PREFIX_LF+'.[N|L]P\d+'


# calType
LABEL_LF = 'load_flow'
LABEL_ST = 'transient_stability'
LABEL_SST_LIN = 'small-signal_stability_linearity'
LABEL_SST_EIG = 'small-signal_stability_eigenvalue'

# getType
LABEL_SETTINGS = 'settings'
LABEL_RESULTS = 'results'

# eleType
LABEL_CONF = 'configuration'
LABEL_BUS = 'bus'
LABEL_ACLINE = 'acline'
LABEL_TRANSFORMER = 'transformer'
LABEL_DCLINE = 'dcline'
LABEL_GENERATOR = 'generator'
LABEL_LOAD = 'load'
LABEL_INTERCHANGE = 'interchange'
LABEL_SVC = 'SVC'
LABEL_FAULT = 'fault'
LABEL_ANA = 'auto_analysis'

LABEL_EIGVAL = 'eigenvalue'
LABEL_EIGVEC= 'eigenvector'

##########
PREFIX_FILE_LF = 'LF'
PREFIX_FILE_ST = 'ST'
POSTFIX_FILE_LF_SETTING = '.L{}'
POSTFIX_FILE_ST_SETTING = '.L{}'
POSTFIX_FILE_LF_RESULT = '.LP{}'
CreatedOnPattern = 'Created on'

Pattern_read = '([^\']*?|\'.*?\')[ ]*,'

StOutVarNameKey = 'var_name'
TimeKey = 'time'
TokenKey = 'token'
RecordMasterDb = 'record_master.db'
RecordLFDb = 'record_lf.db'
RecordMasterTable = 'records'
CompletedLFTable = 'completed_lf'
VarKeyPrefix = 'var_'
VarDefinitionTable = 'VarDef'
VarValueTable = 'VarValue'
#################################################
# ---COMMON---#
MarkKey = 'Mark'
ParNoKey = 'Par_No'
CtrlModeKey = 'Mode_Ctrl'
CtrlBusKey = 'Bus_Ctrl'
CtrlLineKey = 'Line_Ctrl'
CtrlValueKey = 'Value_Ctrl'
INoKey = 'I_No'
JNoKey = 'J_No'
IDNoKey = 'ID_No'
IDKey = 'ID'
R1Key = 'R1'
X1Key = 'X1'
OwnerKey = 'Owner'
UpLimitKey = 'Up_Limit'
LineNameKey = 'Line_Name'

V0Key = 'V0'
AngleKey = 'Angle'
QmaxKey = 'Qmax'
QminKey = 'Qmin'
PmaxKey = 'Pmax'
PminKey = 'Pmin'
ParGroupKey = 'Par_Group'

UnknownDesc = 'Unknown_desc'
UnknownInt = 'Unknown_int'
UnknownFloat_1 = 'Unknown_float'
UnknownFloat_2 = 'Unknown_float'
# ----END----#


# ---BUS---#
BusNoKey = 'Bus_No'
BusNameKey = 'Bus_Name'
BaseKVKey = 'Base_kV'
AreaNoKey = 'Area_No'
VmaxKVKey = 'Vmax_kV'
VminKVKey = 'Vmin_kV'
SC1MVAKey = 'SC1_MVA'
SC3MVAKey = 'SC3_MVA'
# ---END---#

# ---ACLINE---#
ACLineHalfB1Key = 'B1_Half'
ACLineRateKAKey = 'Rate_kA'
# ----END----#

# ---TRANSFORMER---#
TransTkKey = 'Tk'
TransRmKey = 'Rm'
TransXmKey = 'Xm'
Trans2WKey = '2W'
TransTPKey = 'TP'
TransShiftAngKey = 'Ang_Shift'
TransRateMVAKey = 'Rate_MVA'
TransJKey = 'J*'
TransTrsTypeKey = 'TrsType'
TransNameKey = 'Transformer_Name'
TransVi0KVKey = 'Vi0_kV'
TransVj0KVKey = 'Vj0_kV'
TransMaxTapPos2Key = 'Max_Tap2'  # "最高档位2"
TransMinTapPos2Key = 'Min_Tap2'  # "最低档位2"
TransMainTapPos2Key = 'Main_Tap2'  # "主抽头档位2"
TransVjstepPrcKey = 'Vjstep_Prc'
TransVjPosKey = 'Vjpos'
# -------END-------#

# ---DCLINE--#
DCLineRpiKey = 'Rpi_Ohm'
DCLineLpiKey = 'Lpi_mH'
DCLineRpjKey = 'Rpj_Ohm'
DCLineLpjKey = 'Lpj_mH'
DCLineRlKey = 'Rl_Ohm'
DCLineLlKey = 'Ll_mH'
DCLineReiKey = 'Rei_Ohm'
DCLineRejKey = 'Rej_Ohm'
DCLineLsiKey = 'Lsi_mH'
DCLineLsjKey = 'Lsj_mH'
DCLineVdnKey = 'Vdrate_kV'
DCLineVhiKey = 'Vhi_kV'
DCLineVliKey = 'Vli_kV'
DCLineBiKey = 'I_Bridge'
DCLineStiKey = 'Sti_MVA'
DCLineRtiKey = 'Rti_Ohm'
DCLineXtiKey = 'Xti_Perc'
DCLineVtimaxKey = 'Vtimax_kV'
DCLineVtiminKey = 'Vtimin_kV'
DCLineNtapiKey = 'I_Tap'
DCLineVhjKey = 'Vhj_kV'
DCLineVljKey = 'Vlj_Kv'
DCLineBjKey = 'J_Bridge'
DCLineStjKey = 'Stj_MVA'
DCLineRtjKey = 'Rtj_Ohm'
DCLineXtjKey = 'Xtj_Perc'
DCLineVtjmaxKey = 'Vtjmax_kV'
DCLineVtjminKey = 'Vtjmin_kV'
DCLineNtapjKey = 'J_Tap'
DCLineOPKey = 'OP_Mode'
DCLineQciKey = 'Qci_Mvar'
DCLineQcjKey = 'Qcj_Mvar'
DCLinePd1Key = 'Pd1_MW'
DCLineVd1Key = 'Vd1_kV'
DCLineA1minKey = 'A1min_D'
DCLineA10Key = 'A10_D'
DCLineGama1minKey = 'Gam1min_D'
DCLineGama10Key = 'Gam10_D'
DCLinePd2Key = 'Pd2_MW'
DCLineVd2Key = 'Vd2_kV'
DCLineA2minKey = 'A2min_D'
DCLineA20Key = 'A20_D'
DCLineGama2minKey = 'Gam2min_D'
DCLineGama20Key = 'Gam20_D'
# ----END---#

# ---GENERATOR--#
GenPgKey = 'Pg'
GenQgKey = 'Qg'
GenKPrcKey = 'K%'
GenNameKey = 'Generator_Name'
# ------END-----#

# ---LOAD--#
LoadNoKey = 'Load_No'
LoadPlKey = 'Pl'
LoadQlKey = 'Ql'
LoadNameKey = 'Load_Name'
# ---END--#


# ---INTERCHANGE--#
InterchangeAreaNoKey = 'Area_No'
InterchangeAreaNameKey = 'Area_Name'
InterchangeAdjGenKey = 'Gen_Adj'
InterchangeSchedulePKey = 'P_Schedule'
InterchangeToleranceKey = 'Tolerance'
InterchangePmaxKey = 'Pmax'
# -------END------#
#################################################
# ---COMMON---#
VoltageKey = 'V'
PiKey = 'Pi'
QiKey = 'Qi'
PjKey = 'Pj'
QjKey = 'Qj'
# ----END----#

# ---BUS---#
# ---END---#

# ---ACLINE---#
ACLineQciKey = 'Qci'
ACLineQcjKey = 'Qcj'
# ----END----#

# ---TRANSFORMER---#
# -------END-------#

# ---DCLINE--#
DCLineId10Key = 'Id10'
DCLineId20Key = 'Id20'
DCLineVaciKey = 'Vaci'
DCLineVacjKey = 'Vacj'
DCLinePd1iKey = 'Pd1i'
DCLineQd1iKey = 'Qd1i'
DCLineVd10iKey = 'Vd10i'
DCLineTk1iKey = 'Tk1i'
DCLineA10rKey = 'A10r'
DCLineTk1iPercKey = 'Tk1iPerc'
DCLinePd1jKey = 'Pd1j'
DCLineQd1jKey = 'Qd1j'
DCLineVd10jKey = 'Vd10j'
DCLineTk1jKey = 'Tk1j'
DCLineTk1jPercKey = 'Tk1jPerc'
DCLinePd2iKey = 'Pd2i'
DCLineQd2iKey = 'Qd2i'
DCLineVd20iKey = 'Vd20i'
DCLineTk2iKey = 'Tk2i'
DCLineA20rKey = 'A20r'
DCLineTk2iPercKey = 'Tk2iPerc'
DCLinePd2jKey = 'Pd2j'
DCLineQd2jKey = 'Qd2j'
DCLineVd20jKey = 'Vd20j'
DCLineTk2jKey = 'Tk2j'
DCLineTk2jPercKey = 'Tk2jPerc'
DCLineVbiKey = 'Vbi'
DCLineVbjKey = 'Vbj'
DCLineVdbKey = 'Vdb'
DCLineIdbKey = 'Idb'
DCLineZdbKey = 'Zdb'
DCLineLdbKey = 'Ldb'
DCLineTkbiKey = 'Tkbi'
DCLineTkbjKey = 'Tkbj'

DCLineXciKey = 'Xci'
DCLineXcjKey = 'Xcj'
DCLineTkimaxKey = 'Tkimax'
DCLineTkiminKey = 'Tkimin'
DCLineTkjmaxKey = 'Tkjmax'
DCLineTkjminKey = 'Tkjmin'
DCLineQcipKey = 'Qcip'
DCLineQcjpKey = 'Qcjp'
# ----END---#

# ---GENERATOR--#
# ------END-----#

# ---LOAD--#
# ---END--#

# ---INTERCHANGE--#
InterchangePsumKey = 'P_sum'
InterchangeAdjPgKey = 'Pg_adj'
# -------END------#
#################################################
# ---COMMON---#
R0Key = 'R0'
X0Key = 'X0'
# ----END----#

# ---BUS---#
# ---END---#

# ---ACLINE---#
ACLineHalfB0Key = 'B0_Half'
# ----END----#

# ---TRANSFORMER---#
TransTk0Key = 'Tk0'
TransGm0Key = 'Gm0'
TransBm0Key = 'Bm0'
# -------END-------#

# ---DCLINE--#
DCLineModelKey = 'dc_model'  # "直流模型"
DCLineRegTypeKey = 'reg_type'
DCLineRegFonKey = 'reg_fon'
DCLineRegParKey = 'reg_par'
DCLineRegSetKey = 'reg_set'
DCLineAmaxKey = 'Amaxi_D'
DCLineAminKey = 'Amini_D'
DCLineIregFonKey = 'Ireg_fon'
DCLineIregParKey = 'Ireg_par'
DCLineIregSetKey = 'Ireg_set'
DCLineVregFonKey = 'Vreg_fon'
DCLineVregParKey = 'Vreg_par'
DCLineVregSetKey = 'Vreg_set'
DCLineGregFonKey = 'Greg_fon'
DCLineGregParKey = 'Greg_par'
DCLineGregSetKey = 'Greg_set'
DCLineBmaxKey = 'Bmax_D'
DCLineBminKey = 'Bmin_D'
DCLineImKey = 'Im_Percent'
DCLineVLowKey = 'Vlow_Perc'
DCLineIdmaxKey = 'Idmax_kA'
DCLineIdminKey = 'Idmin_ kA'
DCLineDKiKey = 'dKi_Perc'
DCLineDKjKey = 'dKj_Perc'
DCLineDTiKey = 'dTi_s'
DCLineDTjKey = 'dTj_s'
DCLineVRelayKey = 'V_relay_Perc'
DCLineTRelayKey = 'T_relay'
DCLineTypeFdcKey = 'Type_fadc'
DCLineKFdcKey = 'K_fadc'
DCLineTsFdcKey = 'Ts_fadc'
DCLineTeFdcKey = 'Te_fadc'
DCLineTdoKey = 'Tdo'
DCLineTdaKey = 'Tda'
DCLineTdbKey = 'Tdb'
DCLineTdcKey = 'Tdc'
DCLineNRsKey = 'N_rs'
DCLineVRsKey = 'V_rs_Perc'
# ----END---#

# ---GENERATOR--#
GenTgKey = 'GEN_MODEL'
GenLgKey = 'GEN_PAR'
GenTvrKey = 'AVR_MODEL'
GenLvrKey = 'AVR_PAR'
GenTgoKey = 'GOV_MODEL'
GenLgoKey = 'GOV_PAR'
GenTpssKey = 'PSS_MODEL'
GenLpssKey = 'PSS_PAR'
GenXdpKey = 'XDP'
GenXdppKey = 'XDPP'
GenX2Key = 'X2'
GenTjKey = 'TJ'
GenShKey = 'RATE_MVA'
GenPhKey = 'RATE_MW'
# ------END-----#

# ---LOAD--#
LoadModelKey = 'LOAD_MODEL'
LoadParKey = 'LOAD_PAR'
LoadZPercentKey = 'Z_PERCENT'
# ---END--#

# ---SVC--#
SVCSetBusKey = 'Set_Bus'
SVCModelKey = 'SVC_MODEL'
SVCXshKey = 'x_fixed'
SVCAssBus1No = 'ass_bus_1'  # "ass_bus1"
SVCAssBus2No = 'ass_bus_2'  # "ass_bus2"
SVCAssLineNo = 'ass_line'  # "ass_line"
SVCAuxiliarySignal1ValidKey = 'valid_auxiliary_signal_1'  # "辅助信号1有效"
SVCAuxiliarySignal1TypeKey = 'type_auxiliary_signal_1'  # "辅助信号1类型"
SVCAuxiliarySignal2ValidKey = 'valid_auxiliary_signal_2'  # "辅助信号2有效"
SVCAuxiliarySignal2TypeKey = 'type_auxiliary_signal_2'  # "辅助信号2类型"
SVCNameKey = 'SVC_NAME'
# --END--#

#################################################


#################################################
NBusKey = 'NBus'
NACKey = 'Nac'
NTransKey = 'Ntrans'
NDCKey = 'NDC'
NGenKey = 'NGenerator'
NLoadKey = 'NLoad'
NAreaKey = 'Narea'
NUPKey = 'NUP'
NUDKey = 'UD_Time'
NVRKey = 'NVR' # Number of voltage regulator
NGovKey = 'NGov'
NPssKey = 'NPss'
NStaticLoadKey = 'NStaticLoad'
NInductionMotorKey = 'NInductionMotor'
NOtherUDKey = 'NOtherUD'
NStateVariableKey = 'NStateVariable'
NAugmentedStateVariableKey = 'NAugmentedStateVariable'
CtrlUDKey = 'Ctrl_UD'
MatlabIntKey = 'Ctrl_Matitf'
CalDateKey = 'CAL_Date'
CalTimeKey = 'CAL_Time'
MCalKey = 'CALCULATE'

LFNEQKey = 'NEQ'
LFNSSKey = 'NSS'
LFCtrlFactKey = 'Ctrl_Fact'
LFBasicCapacityKey = 'BasicCapacity'
LFVmaxKey = 'Vmax'
LFVminKey = 'Vmin'
LFEpsKey = 'Eps'
LFMethodKey = 'Method'
LFIterationKey = 'Iteration'
LFCtrlAreaKey = 'Ctrl_Area'
LFEQMethodKey = 'EQ_Method'
LFCtrlsubKey = 'Ctrl_sub'
LFUPCALLKey = 'UP_CALL'
LFCtrlRmXmKey = 'Ctrl_RmXm'

LFML23Key = 'L23chged'

STNBPKey = 'NBP'
STNL0Key = 'NL0'
STNT0Key = 'NT0'
STNSVCKey = 'NSVC'
STNFaultKey = 'NFault'
STNDistKey = 'Ndist'
STNM0Key = 'NM0'
STFSKey = 'ST_SC'
STTTotalKey = 'T_Total'
STDTKey = 'DT_Step'
STToutKey = 'Tout'
STMeqKey = 'EQ_Method'
STCeqKey = 'EQ_Continu'
STF60Key = 'F60'
STMutKey = 'Mut'
STF1Key = 'F1'
STCmKey = 'Cm'
STAmaxKey = 'Amax'
STAreaKey = 'Area'
STNUPKey = 'up_cal'
STDErrorKey = 'DError'

STIsStableKey = 'IsStable'
STTimeLoseStableKey = 'Time_lose_stable'
STGroupLoseStableKey = 'Ngroup_lose_stable'

#################################################


#################################################
FaultLocateKey = 'LOCATE'
FaultAddedBusNameKey = 'Add_Name'
FaultPhaseAKey = 'PhaseA'
FaultPhaseBKey = 'PhaseB'
FaultPhaseCKey = 'PhaseC'
FaultGroundKey = 'Ground'
FaultShortKey = 'Short'
FaultOpenKey = 'Open'
FaultTstartKey = 'FaultTstart'
FaultTendKey = 'FaultTend'
FaultRKey = 'FaultR'
FaultXKey = 'FaultX'

#################################################


#################################################
ANALstopKey = 'Lstop'
ANAMaxDAngKey = 'MaxDAng'
ANAMinVolKey = 'MinVol'
ANATDVolKey = 'TDVol'
ANAMinFreqKey = 'MinFreq'
ANATDFreqKey = 'TDFreq'
ANANanaGrpKey = 'NanaGrp'
ANATSDAngKey = 'TSDAng'
#################################################


#################################################
ANATKey = 'ANA_T'
ANAGrpNoKey = 'ANA_GrpNo'
ANAGenAMaxKey = 'ANA_GenAMax'
ANAGenAMinKey = 'ANA_GenAMin'
ANAAngleKey = 'ANA_Angle'
ANABusVMinKey = 'ANA_BusVMin'
ANAVminKey = 'ANA_Vmin'
ANAGenWMinKey = 'ANA_GenWMin'
ANAWMinKey = 'ANA_WMin'
#################################################

#################################################
OutputKeyType = 'var_type'
OutputKeySubType = 'var_subtype'
OutputKeyNoDesc = 'no_desc'
OutputKeyValues = 'values'

#################################################



#################################################
EIGVALNoKey = 'eigen_value_no'
EIGVALRealKey = 'eigen_value_real_part'
EIGVALImgKey = 'eigen_value_image_part'
EIGVALEmprKey = 'elcetro-mechanic_participation_ratio' # "Elcetro-mechanic participation ratio" "机电回路相关比"
#################################################
EIGVECNoKey = 'eigen_value_no'
EIGVECRelatedKey = 'eigenvector_related_ratio'
EIGVECRealKey = 'eigenvector_real_part'
EIGVECImgKey = 'eigenvector_image_part'

# --------------------------------------------------------------------------------------------------------#

#################################################
# TODO: Alter pos_keys of dc,... to multiline
pos_keys_lf_settings_bus = [BusNameKey, BaseKVKey, AreaNoKey, VmaxKVKey, VminKVKey, SC1MVAKey, SC3MVAKey]

pos_keys_lf_settings_acline = [MarkKey, INoKey, JNoKey, IDNoKey, R1Key, X1Key, ACLineHalfB1Key,
                               OwnerKey, CtrlModeKey, ParNoKey, CtrlBusKey, CtrlLineKey,
                               CtrlValueKey, ACLineRateKAKey, UpLimitKey, UnknownDesc, UnknownInt, LineNameKey]

pos_keys_lf_settings_transformer = [MarkKey, INoKey, JNoKey, IDNoKey, R1Key, X1Key,
                                    TransTkKey, TransRmKey, TransXmKey, Trans2WKey,
                                    CtrlModeKey, ParNoKey, TransTPKey, CtrlBusKey, CtrlLineKey, CtrlValueKey,
                                    TransShiftAngKey, TransRateMVAKey, UpLimitKey, IDKey,
                                    TransJKey, TransTrsTypeKey, UnknownDesc, UnknownInt, TransNameKey,
                                    TransVi0KVKey, TransVj0KVKey, TransMaxTapPos2Key, TransMinTapPos2Key,
                                    TransMainTapPos2Key, TransVjstepPrcKey, TransVjPosKey]

pos_keys_lf_settings_dcline = [MarkKey, INoKey, JNoKey, IDNoKey, OwnerKey, LineNameKey, DCLineRpiKey, DCLineLpiKey,
                               DCLineRpjKey, DCLineLpjKey, DCLineRlKey, DCLineLlKey, DCLineReiKey, DCLineRejKey,
                               DCLineLsiKey, DCLineLsjKey, DCLineVdnKey, DCLineVhiKey, DCLineVliKey, DCLineBiKey,
                               DCLineStiKey, DCLineRtiKey, DCLineXtiKey, DCLineVtimaxKey, DCLineVtiminKey,
                               DCLineNtapiKey, DCLineVhjKey, DCLineVljKey, DCLineBjKey, DCLineStjKey, DCLineRtjKey,
                               DCLineXtjKey, DCLineVtjmaxKey, DCLineVtjminKey, DCLineNtapjKey, DCLineOPKey,
                               DCLineQciKey, DCLineQcjKey, DCLinePd1Key, DCLineVd1Key, DCLineA1minKey, DCLineA10Key,
                               DCLineGama1minKey, DCLineGama10Key, DCLinePd2Key, DCLineVd2Key, DCLineA2minKey,
                               DCLineA20Key, DCLineGama2minKey, DCLineGama20Key]

pos_keys_lf_settings_generator = [MarkKey, BusNoKey, CtrlModeKey, GenPgKey, GenQgKey, V0Key, AngleKey,
                                  QmaxKey, QminKey, PmaxKey, PminKey, ParGroupKey,
                                  CtrlBusKey, CtrlLineKey, CtrlValueKey, GenKPrcKey,
                                  UnknownDesc, UnknownInt, GenNameKey]

pos_keys_lf_settings_load = [MarkKey, BusNoKey, LoadNoKey, CtrlModeKey, LoadPlKey, LoadQlKey, V0Key, AngleKey,
                             QmaxKey, QminKey, PmaxKey, PminKey, ParGroupKey, CtrlBusKey, CtrlLineKey, CtrlValueKey,
                             UnknownDesc, UnknownInt, LoadNameKey]

pos_keys_lf_settings_interchange = [MarkKey, InterchangeAreaNoKey, InterchangeAreaNameKey, InterchangeAdjGenKey,
                                    InterchangeSchedulePKey, InterchangeToleranceKey, InterchangePmaxKey]
pos_keys_lf_settings_conf = \
    [NBusKey, NACKey, NTransKey, NDCKey, NGenKey, NLoadKey, NAreaKey, NUDKey, LFNEQKey,
     LFNSSKey, LFCtrlFactKey, LFBasicCapacityKey, LFVmaxKey, LFVminKey, LFEpsKey, LFMethodKey,
     LFIterationKey, LFCtrlAreaKey, CtrlUDKey, LFEQMethodKey, LFCtrlsubKey, LFUPCALLKey, LFCtrlRmXmKey,
     MatlabIntKey]
#################################################

#################################################
pos_keys_lf_results_bus = [BusNoKey, VoltageKey, AngleKey]
pos_keys_lf_results_acline = [INoKey, JNoKey, IDNoKey, PiKey, QiKey, PjKey, QjKey, ACLineQciKey, ACLineQcjKey]
pos_keys_lf_results_transformer = [INoKey, JNoKey, IDNoKey, PiKey, QiKey, PjKey, QjKey]
pos_keys_lf_results_dcline = [INoKey, JNoKey, IDNoKey, OwnerKey, LineNameKey, DCLineOPKey, DCLineId10Key, DCLineId20Key,
                              DCLineVaciKey, DCLineVacjKey, DCLinePd1iKey, DCLineQd1iKey, DCLineVd10iKey, DCLineTk1iKey,
                              DCLineA10rKey, DCLineTk1iPercKey, DCLinePd1jKey, DCLineQd1jKey, DCLineVd10jKey,
                              DCLineTk1jKey, DCLineTk1jPercKey, DCLinePd2iKey, DCLineQd2iKey, DCLineVd20iKey,
                              DCLineTk2iKey, DCLineA20rKey, DCLineTk2iPercKey, DCLinePd2jKey, DCLineQd2jKey,
                              DCLineVd20jKey, DCLineTk2jKey, DCLineTk2jPercKey, DCLineVbiKey, DCLineVbjKey,
                              DCLineVdbKey, DCLineIdbKey, DCLineZdbKey, DCLineLdbKey, DCLineTkbiKey, DCLineTkbjKey,
                              DCLineRpiKey, DCLineLpiKey, DCLineRpjKey, DCLineLpjKey, DCLineRlKey, DCLineLlKey,
                              DCLineReiKey, DCLineRejKey, DCLineLsiKey, DCLineLsjKey, DCLineXciKey, DCLineXcjKey,
                              DCLineTkimaxKey, DCLineTkiminKey, DCLineTkjmaxKey, DCLineTkjminKey, DCLineQcipKey,
                              DCLineQcjpKey, OwnerKey]
pos_keys_lf_results_generator = [BusNoKey, GenPgKey, GenQgKey]
pos_keys_lf_results_load = [BusNoKey, LoadNoKey, LoadPlKey, LoadQlKey]
pos_keys_lf_results_interchange = [AreaNoKey, InterchangePsumKey, InterchangeAdjPgKey]
pos_keys_lf_results_conf = [MCalKey, LFML23Key, CalDateKey, CalTimeKey, NUDKey, NUPKey, NBusKey, NGenKey,
                            NLoadKey, NACKey, NDCKey, NTransKey]

#################################################
pos_keys_st_settings_bus = [BusNameKey]
pos_keys_st_settings_acline = [MarkKey, INoKey, JNoKey, IDNoKey, R0Key, X0Key, ACLineHalfB0Key, LineNameKey]
pos_keys_st_settings_transformer = [MarkKey, INoKey, JNoKey, IDNoKey, R0Key, X0Key, TransTk0Key,
                                    TransGm0Key, TransBm0Key, TransNameKey]
pos_keys_st_settings_dcline = [MarkKey, INoKey, JNoKey, IDNoKey, DCLineModelKey, LineNameKey,
                               DCLineRegTypeKey, DCLineRegFonKey, DCLineRegParKey,
                               DCLineRegSetKey, DCLineAmaxKey, DCLineAminKey, DCLineIregFonKey, DCLineIregParKey,
                               DCLineIregSetKey, DCLineVregFonKey, DCLineVregParKey, DCLineVregSetKey, DCLineGregFonKey,
                               DCLineGregParKey, DCLineGregSetKey, DCLineBmaxKey, DCLineBminKey, DCLineImKey,
                               DCLineVLowKey, DCLineIdmaxKey, DCLineIdminKey, DCLineDKiKey, DCLineDKjKey, DCLineDTiKey,
                               DCLineDTjKey, DCLineVRelayKey, DCLineTRelayKey, DCLineTypeFdcKey, DCLineKFdcKey,
                               DCLineTsFdcKey, DCLineTeFdcKey, DCLineTdoKey, DCLineTdaKey, DCLineTdbKey, DCLineTdcKey,
                               DCLineNRsKey, DCLineVRsKey]
pos_keys_st_settings_generator = [MarkKey, BusNoKey, GenTgKey, GenLgKey, GenTvrKey, GenLvrKey, GenTgoKey, GenLgoKey,
                                  GenTpssKey, GenLpssKey, GenXdpKey, GenXdppKey, GenX2Key, GenTjKey, GenShKey,
                                  GenPhKey, GenNameKey]
pos_keys_st_settings_load = [MarkKey, BusNoKey, LoadNoKey, LoadModelKey, LoadParKey, LoadZPercentKey, LoadNameKey]
pos_keys_st_settings_SVC = [MarkKey, SVCSetBusKey, CtrlBusKey, SVCModelKey, ParNoKey, SVCXshKey,
                            SVCAuxiliarySignal1ValidKey, SVCAuxiliarySignal1TypeKey, SVCAssBus1No, SVCAssBus2No,
                            SVCAssLineNo, SVCAuxiliarySignal2ValidKey, SVCAuxiliarySignal2TypeKey, SVCNameKey]
pos_keys_st_settings_conf = \
    [STNBPKey, STNL0Key, STNT0Key, NDCKey, NGenKey, NLoadKey, STNSVCKey, STNFaultKey,
     STNDistKey, CtrlUDKey, STNM0Key, MatlabIntKey, STFSKey, STTTotalKey, STDTKey, STToutKey, STMeqKey,
     STCeqKey, STF60Key, STMutKey, STF1Key, STCmKey, STAmaxKey, STAreaKey, STNUPKey, STDErrorKey]

pos_keys_st_settings_fault = [MarkKey, INoKey, JNoKey, IDNoKey, FaultLocateKey, FaultAddedBusNameKey,
                              FaultPhaseAKey, FaultPhaseBKey, FaultPhaseCKey, FaultGroundKey,
                              FaultShortKey, FaultOpenKey, FaultTstartKey, FaultTendKey, FaultRKey, FaultXKey]

pos_keys_st_settings_ana = [ANALstopKey, ANAMaxDAngKey, ANAMinVolKey, ANATDVolKey, ANAMinFreqKey, ANATDFreqKey,
                            ANANanaGrpKey, ANATSDAngKey]
#################################################

pos_keys_st_results_conf = [MCalKey, CalDateKey, CalTimeKey, CtrlUDKey, STNUPKey, NBusKey, NGenKey, NLoadKey,
                            NDCKey, STNSVCKey, STNFaultKey, STNDistKey, STIsStableKey, STTimeLoseStableKey,
                            STGroupLoseStableKey]
pos_keys_st_results_ana = [ANATKey, ANAGrpNoKey, ANAGenAMaxKey, ANAGenAMinKey, ANAAngleKey, ANABusVMinKey, ANAVminKey,
                           ANAGenWMinKey, ANAWMinKey]

#################################################
pos_keys_sst_eig_results_eigval = [EIGVALNoKey,EIGVALRealKey,EIGVALImgKey,EIGVALEmprKey]
pos_keys_sst_eig_results_eigenvec = [EIGVECNoKey, BusNoKey, EIGVECRelatedKey, EIGVECRealKey, EIGVECImgKey, BusNameKey]
pos_keys_sst_eig_results_conf = [MCalKey, CalDateKey, CalTimeKey, NBusKey, NGenKey, NVRKey, NGovKey, NPssKey, NDCKey,
                                 NStaticLoadKey, NInductionMotorKey, NOtherUDKey,
                                 NStateVariableKey, NAugmentedStateVariableKey]

#################################################


dict_files_lf_settings = {LABEL_BUS: 'LF.L1', LABEL_ACLINE: 'LF.L2', LABEL_TRANSFORMER: 'LF.L3',
                          LABEL_DCLINE: 'LF.NL4', LABEL_GENERATOR: 'LF.L5', LABEL_LOAD: 'LF.L6',
                          LABEL_INTERCHANGE: 'LF.L7', LABEL_CONF: 'LF.L0'}
dict_files_lf_results = {LABEL_BUS: 'LF.LP1', LABEL_ACLINE: 'LF.LP2', LABEL_TRANSFORMER: 'LF.LP3',
                         LABEL_DCLINE: 'LF.NP4', LABEL_GENERATOR: 'LF.LP5', LABEL_LOAD: 'LF.LP6',
                         LABEL_INTERCHANGE: 'LF.LP7', LABEL_CONF: 'LF.CAL'}
dict_files_st_settings = {LABEL_BUS: 'ST.S1', LABEL_ACLINE: 'ST.S2', LABEL_TRANSFORMER: 'ST.S3',
                          LABEL_DCLINE: 'ST.NS4', LABEL_GENERATOR: 'ST.S5', LABEL_LOAD: 'ST.S6',
                          LABEL_SVC: 'ST.S7', LABEL_CONF: 'ST.S0', LABEL_FAULT: 'ST.S11',
                          LABEL_ANA: 'STCRIT.DAT'}
dict_files_st_results = {LABEL_CONF: 'ST.CAL', LABEL_ANA: 'STANA.DAT'}
dict_files_sst_eig_results = {LABEL_CONF:'SST.CAL',LABEL_EIGVAL: 'SST.EG1',LABEL_EIGVEC: 'SST.EG2'}
dict_files_sst_lin_results = {LABEL_CONF:'SSTLIN.CAL'}

dict_pos_keys_lf_settings = {LABEL_BUS: pos_keys_lf_settings_bus,
                             LABEL_ACLINE: pos_keys_lf_settings_acline,
                             LABEL_TRANSFORMER: pos_keys_lf_settings_transformer,
                             LABEL_DCLINE: pos_keys_lf_settings_dcline,
                             LABEL_GENERATOR: pos_keys_lf_settings_generator,
                             LABEL_LOAD: pos_keys_lf_settings_load,
                             LABEL_INTERCHANGE: pos_keys_lf_settings_interchange,
                             LABEL_CONF: pos_keys_lf_settings_conf}

dict_pos_keys_lf_results = {LABEL_BUS: pos_keys_lf_results_bus,
                            LABEL_ACLINE: pos_keys_lf_results_acline,
                            LABEL_TRANSFORMER: pos_keys_lf_results_transformer,
                            LABEL_DCLINE: pos_keys_lf_results_dcline,
                            LABEL_GENERATOR: pos_keys_lf_results_generator,
                            LABEL_LOAD: pos_keys_lf_results_load,
                            LABEL_INTERCHANGE: pos_keys_lf_results_interchange,
                            LABEL_CONF: pos_keys_lf_results_conf}

dict_pos_keys_st_settings = {LABEL_BUS: pos_keys_st_settings_bus,
                             LABEL_ACLINE: pos_keys_st_settings_acline,
                             LABEL_TRANSFORMER: pos_keys_st_settings_transformer,
                             LABEL_DCLINE: pos_keys_st_settings_dcline,
                             LABEL_GENERATOR: pos_keys_st_settings_generator,
                             LABEL_LOAD: pos_keys_st_settings_load,
                             LABEL_SVC: pos_keys_st_settings_SVC,
                             LABEL_CONF: pos_keys_st_settings_conf,
                             LABEL_ANA: pos_keys_st_settings_ana,
                             LABEL_FAULT: pos_keys_st_settings_fault}

dict_pos_keys_st_results = {LABEL_CONF: pos_keys_st_results_conf,
                            LABEL_ANA: pos_keys_st_results_ana}

dict_pos_keys_sst_eig_results = {LABEL_EIGVAL: pos_keys_sst_eig_results_eigval,
                                 LABEL_EIGVEC: pos_keys_sst_eig_results_eigenvec,
                                 LABEL_CONF: pos_keys_sst_eig_results_conf}

dict_multiline = {dict_files_lf_settings[LABEL_DCLINE]: 8,
                  dict_files_lf_results[LABEL_DCLINE]: 10,
                  dict_files_st_settings[LABEL_DCLINE]: 5,
                  dict_files_lf_settings[LABEL_CONF]: True,
                  dict_files_st_settings[LABEL_CONF]: True,
                  dict_files_lf_results[LABEL_CONF]: True,
                  dict_files_st_results[LABEL_CONF]: True}
files_lf_append_no = [dict_files_lf_settings[LABEL_BUS],
                      dict_files_st_settings[LABEL_BUS]]

dict_mapping_files = {LABEL_LF: {LABEL_SETTINGS: dict_files_lf_settings, LABEL_RESULTS: dict_files_lf_results},
                      LABEL_ST: {LABEL_SETTINGS: dict_files_st_settings, LABEL_RESULTS: dict_files_st_results},
                      LABEL_SST_EIG: {LABEL_RESULTS: dict_files_sst_eig_results},
                      LABEL_SST_LIN: {LABEL_RESULTS: dict_files_sst_lin_results}}
dict_mapping_pos_keys = {LABEL_LF: {LABEL_SETTINGS: dict_pos_keys_lf_settings, LABEL_RESULTS: dict_pos_keys_lf_results},
                         LABEL_ST: {LABEL_SETTINGS: dict_pos_keys_st_settings, LABEL_RESULTS: dict_pos_keys_st_results},
                         LABEL_SST_EIG: {LABEL_RESULTS:dict_pos_keys_sst_eig_results}}



'''
dict_types = {
    int: [Trans2WKey, TransMainTapPos2Key, TransTrsTypeKey, UnknownInt, JNoKey, InterchangeAreaNoKey, LoadNoKey,
          GenKPrcKey, TransVjPosKey, InterchangeAdjGenKey, DCLineBiKey, DCLineBjKey, MarkKey, IDKey,
          TransMaxTapPos2Key, ParGroupKey, TransJKey, DCLineOPKey, TransMinTapPos2Key, BusNoKey, CtrlBusKey, INoKey,
          OwnerKey, CtrlModeKey, IDNoKey, ParNoKey, CtrlLineKey, DCLineRegTypeKey, DCLineRegFonKey, DCLineRegParKey,
          DCLineIregFonKey, DCLineIregParKey, DCLineVregParKey, DCLineGregParKey,
          DCLineNRsKey, GenTgKey, GenLgKey, GenTvrKey, GenLvrKey, GenTgoKey, GenLgoKey,
          GenTpssKey, GenLpssKey, LoadModelKey, LoadParKey, LoadZPercentKey, SVCSetBusKey, SVCModelKey, DCLineModelKey,
          DCLineKFdcKey, DCLineVregFonKey, DCLineGregFonKey, DCLineTypeFdcKey, SVCAssBus1No, SVCAssBus2No, SVCAssLineNo,
          SVCAuxiliarySignal1ValidKey, SVCAuxiliarySignal1TypeKey, SVCAuxiliarySignal2ValidKey,
          SVCAuxiliarySignal2TypeKey, STNBPKey, STNL0Key, STNT0Key, NDCKey, NGenKey, NLoadKey, STNSVCKey,
          STNFaultKey, STNDistKey, CtrlUDKey, STNM0Key, MatlabIntKey, STFSKey, STMeqKey, STCeqKey, STF60Key, STMutKey,
          STF1Key, STCmKey, STAreaKey, STNUPKey, NBusKey, NACKey, NTransKey, NUPKey, STNFaultKey, STNDistKey,
          NAreaKey, LFNEQKey, LFNSSKey, LFCtrlFactKey, LFMethodKey, LFIterationKey, LFCtrlAreaKey,
          LFEQMethodKey, LFCtrlsubKey, LFUPCALLKey, LFCtrlRmXmKey, MCalKey, STIsStableKey, STGroupLoseStableKey,
          LFML23Key, NUDKey, FaultLocateKey, FaultAddedBusNameKey, FaultPhaseAKey, FaultPhaseBKey, FaultPhaseCKey,
          FaultGroundKey, FaultShortKey, FaultOpenKey, ANANanaGrpKey, ANALstopKey, ANATKey, ANAAngleKey,
          ANAVminKey, ANAWMinKey,EIGVALNoKey],
    convert2float_s: [TransShiftAngKey, DCLineVljKey, DCLineVtiminKey, DCLinePd1Key, DCLineReiKey, DCLineStiKey,
                      DCLineA2minKey, LoadQlKey, DCLineLpjKey, VmaxKVKey, DCLineVd2Key, DCLineA20Key, BaseKVKey,
                      DCLineStjKey, DCLineRpjKey, ACLineRateKAKey, DCLineXtiKey, DCLineRlKey, TransTPKey,
                      TransRateMVAKey, DCLineXtjKey, TransTkKey, GenQgKey, DCLineRtjKey, R1Key, TransVjstepPrcKey,
                      DCLineGama20Key, QmaxKey, TransRmKey, TransXmKey, DCLineLsiKey, DCLineLsjKey, DCLineGama1minKey,
                      DCLineVtjminKey, V0Key, DCLineQcjKey, DCLineNtapiKey, DCLineQciKey, PminKey, AngleKey,
                      ACLineHalfB1Key, DCLineLlKey, UpLimitKey, DCLineVtjmaxKey, DCLineNtapjKey, DCLineVhjKey,
                      DCLineRejKey, DCLineGama10Key, DCLineA1minKey, InterchangeToleranceKey, TransVj0KVKey,
                      InterchangePmaxKey, DCLineRpiKey, DCLineRtiKey, LoadPlKey, DCLineGama2minKey, DCLineLpiKey,
                      DCLineVd1Key, DCLineVtimaxKey, SC1MVAKey, GenPgKey, DCLineA10Key, DCLineVhiKey, TransVi0KVKey,
                      DCLinePd2Key, VminKVKey, CtrlValueKey, DCLineVliKey, SC3MVAKey, X1Key, QminKey, DCLineVdnKey,
                      InterchangeSchedulePKey, VoltageKey, PiKey, QiKey, PjKey, QjKey, ACLineQciKey, ACLineQcjKey,
                      DCLineId10Key, DCLineId20Key, DCLineVaciKey, DCLineVacjKey, DCLinePd1iKey, DCLineQd1iKey,
                      DCLineVd10iKey, DCLineTk1iKey, DCLineA10rKey, DCLineTk1iPercKey, DCLinePd1jKey, DCLineQd1jKey,
                      DCLineVd10jKey, DCLineTk1jKey, DCLineTk1jPercKey, DCLinePd2iKey, DCLineQd2iKey, DCLineVd20iKey,
                      DCLineTk2iKey, DCLineA20rKey, DCLineTk2iPercKey, DCLinePd2jKey, DCLineQd2jKey, DCLineVd20jKey,
                      DCLineTk2jKey, DCLineTk2jPercKey, DCLineVbiKey, DCLineVbjKey, DCLineVdbKey, DCLineIdbKey,
                      DCLineZdbKey, DCLineLdbKey, DCLineTkbiKey, DCLineTkbjKey, DCLineXciKey, DCLineXcjKey,
                      DCLineTkimaxKey, DCLineTkiminKey, DCLineTkjmaxKey, DCLineTkjminKey, DCLineQcipKey, DCLineQcjpKey,
                      InterchangePsumKey, InterchangeAdjPgKey, R0Key, X0Key, ACLineHalfB0Key, TransTk0Key,
                      DCLineRegSetKey, DCLineAmaxKey, DCLineAminKey, DCLineBmaxKey,
                      DCLineBminKey, DCLineImKey, DCLineVLowKey, DCLineIdmaxKey, DCLineIdminKey, DCLineDKiKey,
                      DCLineDKjKey, DCLineDTiKey, DCLineDTjKey, DCLineVRelayKey, DCLineTRelayKey,
                      DCLineTsFdcKey, DCLineTeFdcKey, DCLineTdaKey, DCLineTdbKey, DCLineTdcKey,
                      DCLineVRsKey, GenXdpKey, GenXdppKey, GenX2Key, GenTjKey, GenShKey, GenPhKey, SVCXshKey,
                      DCLineTdoKey, DCLineGregSetKey, TransGm0Key, TransBm0Key, DCLineIregSetKey, DCLineVregSetKey,
                      STTTotalKey, STDTKey, STToutKey, STAmaxKey, STDErrorKey,
                      LFBasicCapacityKey, LFVmaxKey, LFVminKey, LFEpsKey, STTimeLoseStableKey,
                      FaultTstartKey, FaultTendKey, FaultRKey, FaultXKey, ANAMaxDAngKey, ANAMinVolKey,
                      ANATDVolKey, ANAMinFreqKey, ANATDFreqKey, ANATSDAngKey,
                      ANAGrpNoKey, ANAGenAMaxKey, ANAGenAMinKey, ANABusVMinKey, ANAGenWMinKey,
                      EIGVALRealKey,EIGVALImgKey,EIGVALEmprKey],
    None: [TransNameKey, InterchangeAreaNameKey, GenNameKey, LineNameKey, BusNameKey, UnknownDesc,
           LoadNameKey, SVCNameKey, CalDateKey, CalTimeKey]
}

dict_translate = {kk: v for v, k in dict_types.items() for kk in k}
'''





'''
LFL1 = ['NULL1               ',    0.0000,   0,    0.0000,    0.0000,    0.0000,    0.0000]
LFL2 = [1,     4,     3,     0,       0.000000,       0.000010,       0.000000,   0, 0, 0,   0,   0,      0.000000,      0.000000,  0.00,'                        ',  15,'AC_5_8_0_ac']
LFL3 = [1,     5,     4,301156,       0.000090,       0.017864,       1.021430,       0.000000,       0.000000,   0,   0,   0,   0,   0,   0,       0.000000,       0.000000,     810.000000,  0.00, 0, 0, 1,'                        ',  15,'T2W301156_2w_2w         ',      20.000000,     550.000000,  1,  3,  1,       2.500000,  2]
LFNL4 = [1,24526,17591,1000,4001,'DC1000',0.000000,0.000000,0.000000,0.000000,12.600000,1590.000000,0.000000,0.000000,300.000000,300.000000,800.000000,530.000000,170.300003,4,3853.000000,0.000000,18.000000,682.375000,496.880005,29,525.000000,157.600006,4,3565.000000,0.000000,16.700001,637.500000,468.799988,28,20,0.000000,0.000000,800.000000,800.000000,5.000000,15.000000,8.000000,17.000000,800.000000,800.000000,5.000000,15.000000,8.000000,17.000000]
LFL5 = [1,    10,   0,       7.600000,       1.000000,       0.980000,       0.000000,       3.000000,       0.500000,       7.600000,       0.000000,   0,   0,   0,       0.000000,  0,'                        ',  15,'鄂三峡左#07']
LFL6 = [1,    11,     0,   1,       6.000000,       0.000000,       1.000000,       0.000000,       0.000000,       0.000000,       0.000000,       0.000000,   1,   0,   0,       0.000000,'                        ',  15,'鄂龙泉5000']
LFL7 = [1,	0,		'全网                              ',	0,		0,		0,		0]

maps = [(LFL1,pos_lf_bus),(LFL2,pos_lf_acline),(LFL3,pos_lf_transformer),(LFNL4,pos_lf_dcline),(LFL5,pos_lf_generator),
        (LFL6,pos_lf_load), (LFL7,pos_lf_interchange)]
dict_types = {}
dicts = []

for t in maps:
    LF_t = t[0]
    pos_t = t[1]
    if len(LF_t)!=len(pos_t):
        print('length not equal')
    dict_t = {pos_t[h]:LF_t[h] for h in range(len(LF_t))}
    list_type = [type(v) for v in dict_t.values()]
    types = set(list_type)
    for type_t in types:
        list_t = [k for k,v in dict_t.items() if isinstance(v,type_t)]
        if type_t in dict_types.keys():
            dict_types[type_t].extend(list_t)
        else:
            dict_types[type_t] = list_t.copy()
    dicts.append(dict_t)

dict_types = {k:list(set(v)) for k,v in dict_types.items()}
dict_intersection = {}
for k1,v1 in dict_types.items():
    for k2,v2 in dict_types.items():
        if k1!=k2:
            k_t = (k1,k2)
            if k_t not in dict_intersection.keys():
                dict_intersection[k_t] = set(v1).intersection(set(v2))

keys_float = ['I_tap','J_tap','Tolerance','TP','Pmax']
dict_types[int] = list(set(dict_types[int]).difference(keys_float))
dict_types[float].extend(keys_float)
dict_types[float] = list(set(dict_types[float]))


print(dict_types[int])
print(dict_types[float])
print(dict_types[str])
'''
'''
TT = ['reg_type','reg_fon','reg_par','reg_set','Amax','Amin','Ireg_fon','Ireg_par','Ireg_set','Vreg_fon','Vreg_par','Vreg_set','Greg_fon','Greg_par','Greg_set','Bmax','Bmin','Im','V_low','Idmax','Idmin','dKi','dKj','dTi','dTj','V_relay','T_relay','Type_fdc','K_fdc','Ts_fdc','Te_fdc','Tdo','Tda','Tdb','Tdc','N_rs','V_rs','Tg','Lg','Tvr','Lvr','Tgo','Lgo','Tpss','Lpss','Xdp','Xdpp','X2','Tj','Sh','Ph']
for h in range(len(TT)):
     str_t = TT[h]
     list_str_t = str_t.split('_')
     list_str_new = []
     for str_tt in list_str_t:
         str_tt_new = str_tt[0].upper()
         if len(str_tt)>1:
             str_tt_new+=str_tt[1:]
         list_str_new.append(str_tt_new)
     tt = ''.join(list_str_new)
     TT[h] = tt
print(TT)
'''