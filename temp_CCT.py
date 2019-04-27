from PyPSASP.PSASPClasses.PSASP import CCT_generator,func_change_lf_temp
from PyPSASP.constants import const
import os, traceback

PATH_TEMP = r'E:\LXZ\PythonWorks\PowerSystem\Temp_20190419'
PATH_RESOURCES = PATH_TEMP
PATH_OUTPUT = r'E:\LXZ\Data\Research\PyPSASP\CCT\3m'

os.system('@echo off')
Cc = CCT_generator(PATH_TEMP, PATH_RESOURCES, PATH_OUTPUT, func_change_lf_temp)
count_t = 0
max_count = 10000
while count_t <= max_count:
    try:
        rec_t = Cc.run_sim_CCT_once()
        count_t += 1
    except:
        traceback.print_exc()

