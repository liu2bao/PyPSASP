import os
import re
from PyPSASP.utils.utils_gadgets import copyfiles,copyfiles_pattern
from PyPSASP.constants.const import FILE_STOUT, dict_files_st_settings, LABEL_CONF, dict_files_st_results, LABEL_ANA
from PyPSASP.constants.const import FILE_PREFIX_LF,PATTERN_OUTPUT_ST,PATTERN_SETTINGS_LF,PATTERN_RESULTS_LF


def copyfiles_st(path_src,path_dst):
    if os.path.isdir(path_src):
        ST_conf = {FILE_STOUT,
                   dict_files_st_settings[LABEL_CONF],
                   dict_files_st_results[LABEL_CONF],
                   dict_files_st_results[LABEL_ANA]}
        files_t = os.listdir(path_src)
        files_part_1 = list(set(files_t).intersection(ST_conf))
        files_part_2 = [x for x in files_t if re.match(PATTERN_OUTPUT_ST,x)]
        files_st = files_part_1+files_part_2
        copyfiles(path_src,path_dst,files_st)


def copyfiles_lf(path_src,path_dst):
    if os.path.isdir(path_src):
        files_lf = [x for x in os.listdir(path_src) if x.startswith(FILE_PREFIX_LF)]
        copyfiles(path_src,path_dst,files_lf)


def copyfiles_lfs(path_src,path_dst):
    copyfiles_pattern(path_src,path_dst,PATTERN_SETTINGS_LF)


def copyfiles_lfr(path_src,path_dst):
    copyfiles_pattern(path_src,path_dst,PATTERN_RESULTS_LF)


if __name__=='__main__':
    path_src_t = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190422_MinInputs'
    path_dst_t = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190422_MinInputs\temp'
    copyfiles_st(path_src_t, path_dst_t)