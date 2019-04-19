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

Pattern_read = '([^\']*?|\'.*?\'),'

MarkKey = 'Mark'

#########---BUS---#########
BusNoKey = 'Bus_No'
BusNameKey = 'Bus_Name'
BaseKVKey = 'Base_kV'
AreaNoKey = 'Area_No'
VmaxKVKey = 'Vmax_kV'
VminKVKey = 'Vmin_kV'
SC1MVAKey = 'SC1_MVA'
SC3MVAKey = 'SC3_MVA'
#########---ACLINE---#########
ACLineINameKey = 'I_Name'
ACLineJNameKey = 'J_Name'
ACLineIDNoKey = 'ID_No'
ACLineR1Key = 'R1'
ACLineX1Key = 'X1'
ACLineHalfB1Key = 'B1_Half'
ACLineOwnerKey = 'Owner'
ACLineCtrlModeKey = 'Mode_Ctrl'
ACLineParNoKey = 'Par_No'
ACLineCtrlBusKey = 'Bus_Ctrl'
ACLineCtrlLineKey = 'Line_Ctrl'
ACLineCtrlValueKey = 'Value_Ctrl'
ACLineRateKAKey = 'Rate_kA'
ACLineUpLimitKey = 'Up_Limit'
ACLineNameKey = 'Line_Name'

UnknownDesc = 'Unknown_desc'
UnknownInt = 'Unknown_int'
#########---TRANSFORMER---#########
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
TransMaxTapPos2Key = 'Max_Tap2' # "最高档位2"
TransMinTapPos2Key = 'Min_Tap2' # "最低档位2"
TransMainTapPos2Key = 'Main_Tap2' # "主抽头档位2"
TransVjstepPrcKey = 'Vjstep_Prc'
TransVjPosKey = 'Vjpos'

pos_lf_bus = [BusNameKey, BaseKVKey, AreaNoKey, VmaxKVKey, VminKVKey, SC1MVAKey, SC3MVAKey, convert2float_s]
pos_lf_acline = [MarkKey, ACLineINameKey, ACLineJNameKey, ACLineIDNoKey, ACLineR1Key, ACLineX1Key, ACLineHalfB1Key,
                 ACLineOwnerKey, ACLineCtrlModeKey, ACLineParNoKey, ACLineCtrlBusKey, ACLineCtrlLineKey,
                 ACLineCtrlValueKey, ACLineRateKAKey, ACLineUpLimitKey, UnknownDesc, UnknownInt, ACLineNameKey]


pos_lf_transformer = [MarkKey, ACLineINameKey, ACLineJNameKey, ACLineIDNoKey, ACLineR1Key, ACLineX1Key,
                      TransTkKey, TransRmKey, TransXmKey, Trans2WKey,
                      ACLineCtrlModeKey, ACLineParNoKey, TransTPKey, ACLineCtrlBusKey, ACLineCtrlLineKey,
                      ACLineCtrlValueKey, TransShiftAngKey, TransRateMVAKey, ACLineUpLimitKey, TransIDKey,
                      TransJKey, TransTrsTypeKey,UnknownDesc, UnknownInt, TransNameKey,
                      TransVi0KVKey, TransVj0KVKey, TransMaxTapPos2Key,TransMinTapPos2Key,TransMainTapPos2Key,
                      TransVjstepPrcKey,TransVjPosKey]


dict_translate_lf_bus = {BusNameKey: None,
                         BaseKVKey: convert2float_s,
                         AreaNoKey: convert2float_s,
                         VmaxKVKey: convert2float_s,
                         VminKVKey: convert2float_s,
                         SC1MVAKey: convert2float_s,
                         SC3MVAKey: convert2float_s}

dict_translate_lf_common_acline_trans = {MarkKey: int,
                                         ACLineINameKey: int,
                                         ACLineJNameKey: int,
                                         ACLineIDNoKey: int,
                                         ACLineR1Key: convert2float_s,
                                         ACLineX1Key: convert2float_s}

# TODO: Some colomns are short here
dict_translate_lf_acline = dict_translate_lf_common_acline_trans.copy()
dict_translate_lf_acline.update({ACLineHalfB1Key: convert2float_s,
                                 ACLineOwnerKey: int,
                                 ACLineCtrlModeKey: int,
                                 ACLineParNoKey: int,
                                 ACLineCtrlBusKey: int,
                                 ACLineCtrlLineKey: int,
                                 ACLineCtrlValueKey: convert2float_s,
                                 ACLineRateKAKey: convert2float_s,
                                 ACLineUpLimitKey: convert2float_s,
                                 UnknownDesc: None,
                                 UnknownInt: int,
                                 ACLineNameKey: None})

dict_translate_lf_transformer = dict_translate_lf_common_acline_trans.copy()
dict_translate_lf_transformer.update({})
