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

BusNoKey = 'Bus_No'
BusNameKey = 'Bus_Name'
BaseKVKey = 'Base_kV'
AreaNoKey = 'Area_No'
VmaxKVKey = 'Vmax_kV'
VminKVKey = 'Vmin_kV'
SC1MVAKey = 'SC1_MVA'
SC3MVAKey = 'SC3_MVA'

LineINameKey = 'I_Name'
LineJNameKey = 'J_Name'
LineIDNoKey = 'ID_No'
LineR1Key = 'R1'
LineX1Key = 'X1'
LineHalfB1Key = 'B1_Half'
LineOwnerKey = 'Owner'
LineCtrlModeKey = 'Mode_Ctrl'
LineParNoKey = 'Par_No'
LineCtrlBusKey = 'Bus_Ctrl'
LineCtrlLineKey = 'Line_ctrl'
LineCtrlValueKey = 'Value_Ctrl'
LineRateKAKey = 'Rate_kA'
LineUpLimitKey = 'Up_limit'

dict_translate_lf_bus = {BusNameKey: None,
                         BaseKVKey: convert2float_s,
                         AreaNoKey: convert2float_s,
                         VmaxKVKey: convert2float_s,
                         VminKVKey: convert2float_s,
                         SC1MVAKey: convert2float_s,
                         SC3MVAKey: convert2float_s}

dict_translate_lf_line = {LineINameKey: int,
                          LineJNameKey: int,
                          LineIDNoKey: int,
                          LineR1Key: convert2float_s,
                          LineX1Key: convert2float_s,
                          LineHalfB1Key: convert2float_s,
                          LineOwnerKey: int,
                          LineCtrlModeKey: int,
                          LineParNoKey: int,
                          LineCtrlBusKey: int,
                          LineCtrlLineKey: int,
                          LineCtrlValueKey: convert2float_s,
                          LineRateKAKey: convert2float_s,
                          LineUpLimitKey: convert2float_s}
