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

FILE_TEMPLATE = lambda prefix,postfix,x:(prefix+postfix).format(x)
FILE_TEMPLATE_LF = lambda postfix,x:FILE_TEMPLATE(PREFIX_FILE_LF,postfix,x)
FILE_TEMPLATE_LF_SETTING = lambda x:FILE_TEMPLATE_LF(POSTFIX_FILE_LF_SETTING,x)
FILE_TEMPLATE_LF_RESULT = lambda x:FILE_TEMPLATE_LF(POSTFIX_FILE_LF_RESULT,x)

DICT_FILES_LF = {}

