from PyPSASP.PSASPClasses.PSASP import CCT_generator,func_change_lf_temp
from PyPSASP.constants import const
import os, traceback

'''
if __name__=='__main__':
    from PyPSASP.PSASPClasses.Parsers import PSASP_Parser
    from PyPSASP.PSASPClasses.Writers import PSASP_Writer

    path_temp = r'E:\01_Research\98_Data\SmallSystem_PSASP\SMIB\2016_06_01T00_00_24'
    path_temp_2 = r'E:\01_Research\98_Data\SmallSystem_PSASP\SMIB\2016_06_01T00_00_24_copy'
    Parser_t = PSASP_Parser(path_temp)
    Writer_t = PSASP_Writer(path_temp_2)
    T = Parser_t.parse_all_parsable()
    Writer_t.write_all_writable(T)
'''

PATH_TEMP = r'E:\LXZ\PythonWorks\PowerSystem\Temp_20190419'
PATH_RESOURCES = PATH_TEMP
PATH_OUTPUT = r'E:\Data\Research\PyPSASP\CCT\3m'

os.system('@echo off')
Cc = CCT_generator(PATH_TEMP, PATH_RESOURCES, PATH_OUTPUT, func_change_lf_temp)
count_t = 0
max_count = 10000
while count_t <= max_count:
    try:
        Cc.run_sim_CCT_once()
        count_t += 1
    except:
        traceback.print_exc()

