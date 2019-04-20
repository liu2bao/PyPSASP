from Gadgets_PSASP import convert2float_s

EXE_LF = 'WMLFRTMsg.exe'
EXE_ST = 'wmudrt.exe'

LABEL_LF = 'load_flow'
LABEL_ST = 'transient_stability'

LABEL_BUS = 'bus'
LABEL_ACLINE = 'acline'
LABEL_TRANSFORMER = 'transformer'
LABEL_DCLINE = 'dcline'
LABEL_GENERATOR = 'generator'
LABEL_LOAD = 'load'

PREFIX_FILE_LF = 'LF'
PREFIX_FILE_ST = 'ST'
POSTFIX_FILE_LF_SETTING = '.L{}'
POSTFIX_FILE_ST_SETTING = '.L{}'
POSTFIX_FILE_LF_RESULT = '.LP{}'

FILE_TEMPLATE = lambda prefix, postfix, x: (prefix + postfix).format(x)
FILE_TEMPLATE_LF = lambda postfix, x: FILE_TEMPLATE(PREFIX_FILE_LF, postfix, x)
FILE_TEMPLATE_LF_SETTING = lambda x: FILE_TEMPLATE_LF(POSTFIX_FILE_LF_SETTING, x)
FILE_TEMPLATE_LF_RESULT = lambda x: FILE_TEMPLATE_LF(POSTFIX_FILE_LF_RESULT, x)

DICT_FILES_LF = {POSTFIX_FILE_LF_RESULT: FILE_TEMPLATE_LF_RESULT}
DICT_FILES_ST = {POSTFIX_FILE_LF_RESULT: FILE_TEMPLATE_LF_RESULT}

Pattern_read = '([^\']*?|\'.*?\')[ ]*,'

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
TransIDKey = 'ID'
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
pos_keys_lf_settings_bus = [BusNameKey, BaseKVKey, AreaNoKey, VmaxKVKey, VminKVKey, SC1MVAKey, SC3MVAKey]

pos_keys_lf_settings_acline = [MarkKey, INoKey, JNoKey, IDNoKey, R1Key, X1Key, ACLineHalfB1Key,
                               OwnerKey, CtrlModeKey, ParNoKey, CtrlBusKey, CtrlLineKey,
                               CtrlValueKey, ACLineRateKAKey, UpLimitKey, UnknownDesc, UnknownInt, LineNameKey]

pos_keys_lf_settings_transformer = [MarkKey, INoKey, JNoKey, IDNoKey, R1Key, X1Key,
                                    TransTkKey, TransRmKey, TransXmKey, Trans2WKey,
                                    CtrlModeKey, ParNoKey, TransTPKey, CtrlBusKey, CtrlLineKey, CtrlValueKey,
                                    TransShiftAngKey, TransRateMVAKey, UpLimitKey, IDNoKey,
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
                             UnknownDesc, UnknownInt, GenNameKey]

pos_keys_lf_settings_interchange = [MarkKey, InterchangeAreaNoKey, InterchangeAreaNameKey, InterchangeAdjGenKey,
                                    InterchangeSchedulePKey, InterchangeToleranceKey, InterchangePmaxKey]
#################################################
# --------------------------------------------------------------------------------------------------------#
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

#################################################


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

dict_types = {
    int: [Trans2WKey, TransMainTapPos2Key, TransTrsTypeKey, UnknownInt, JNoKey, InterchangeAreaNoKey, LoadNoKey,
          GenKPrcKey, TransVjPosKey, InterchangeAdjGenKey, DCLineBiKey, DCLineBjKey, MarkKey, TransIDKey,
          TransMaxTapPos2Key, ParGroupKey, TransJKey, DCLineOPKey, TransMinTapPos2Key, BusNoKey, CtrlBusKey, INoKey,
          OwnerKey, CtrlModeKey, IDNoKey, ParNoKey, CtrlLineKey],
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
                      InterchangePsumKey, InterchangeAdjPgKey],
    None: [TransNameKey, InterchangeAreaNameKey, GenNameKey, LineNameKey, BusNameKey, UnknownDesc]
}

dict_translate_lf = {kk: v for v, k in dict_types.items() for kk in k}

file_lf_settings_bus = 'LF.L1'
file_lf_settings_acline = 'LF.L2'
file_lf_settings_transformer = 'LF.L3'
file_lf_settings_dcline = 'LF.NL4'
file_lf_settings_gen = 'LF.L5'
file_lf_settings_load = 'LF.L6'
file_lf_settings_interchange = 'LF.L7'
dict_pos_keys_lf_settings = {file_lf_settings_bus: pos_keys_lf_settings_bus,
                             file_lf_settings_acline: pos_keys_lf_settings_acline,
                             file_lf_settings_transformer: pos_keys_lf_settings_transformer,
                             file_lf_settings_dcline: pos_keys_lf_settings_dcline,
                             file_lf_settings_gen: pos_keys_lf_settings_generator,
                             file_lf_settings_load: pos_keys_lf_settings_load,
                             file_lf_settings_interchange: pos_keys_lf_settings_interchange}

file_lf_results_bus = 'LF.LP1'
file_lf_results_acline = 'LF.LP2'
file_lf_results_transformer = 'LF.LP3'
file_lf_results_dcline = 'LF.NP4'
file_lf_results_gen = 'LF.LP5'
file_lf_results_load = 'LF.LP6'
file_lf_results_interchange = 'LF.LP7'
dict_pos_keys_lf_results = {file_lf_results_bus: pos_keys_lf_results_bus,
                            file_lf_results_acline: pos_keys_lf_results_acline,
                            file_lf_results_transformer: pos_keys_lf_results_transformer,
                            file_lf_results_dcline: pos_keys_lf_results_dcline,
                            file_lf_results_gen: pos_keys_lf_results_generator,
                            file_lf_results_load: pos_keys_lf_results_load,
                            file_lf_results_interchange: pos_keys_lf_results_interchange}

dict_multiline_lf = {file_lf_settings_dcline: 8,
                     file_lf_results_dcline: 10}
files_lf_append_no = [file_lf_settings_bus]