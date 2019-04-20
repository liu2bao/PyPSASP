import Gadgets_PSASP
import const
import math
import re
import os


def parse_lines_PSASP(lines, pos_keys, dict_translate=const.dict_translate_lf,
                      pattern_parse=const.Pattern_read, multi_line=1, key_busno=None):
    lines_t = lines.copy()
    if str.find(lines_t[0], 'Created on') != -1:
        list.pop(lines_t, 0)

    if multi_line > 1:
        num_lines = len(lines_t)
        Ndiv = math.ceil(num_lines / multi_line)
        lines_t = [''.join([lines_t[hh] for hh in range(h * multi_line, (h + 1) * multi_line)]) for h in range(Ndiv)]

    list_dict_parsed = []
    append_no = isinstance(key_busno, str)
    for h in range(len(lines_t)):
        line_t = lines_t[h]
        if isinstance(line_t, str):
            contents = re.findall(pattern_parse, line_t)
            if contents:
                dict_t = {}
                for hh in range(min([len(contents), len(pos_keys)])):
                    key_t = pos_keys[hh]
                    trans_func_t = dict_translate[key_t]
                    if trans_func_t:
                        vt = trans_func_t(contents[hh])
                    else:
                        vt = contents[hh]
                    dict_t[key_t] = vt
                if append_no:
                    dict_t[key_busno] = h
                list_dict_parsed.append(dict_t)

    return list_dict_parsed


def parse_lf(path_lf, lfs_check=None, dict_pos_keys_lf=const.dict_pos_keys_lf_settings):
    suppath_t, lf_t = os.path.split(path_lf)
    if lfs_check is None or lf_t in lfs_check:
        if os.path.isfile(path_lf):
            with open(path_lf, 'r') as f:
                lines_raw = f.readlines()
            lines = [x.strip() for x in lines_raw]
            if lines:
                if lf_t in const.dict_multiline_lf.keys():
                    multi_line = const.dict_multiline_lf[lf_t]
                else:
                    multi_line = 1
                if lf_t in const.files_lf_append_no:
                    key_busno = const.BusNoKey
                else:
                    key_busno = None

                list_dict_parsed = parse_lines_PSASP(lines, dict_pos_keys_lf[lf_t],
                                                     multi_line=multi_line, key_busno=key_busno)
                return list_dict_parsed
    else:
        return None


def parse_lf_all_settings(path_temp, dict_pos_keys_lf=const.dict_pos_keys_lf_settings):
    lf_settings = list(dict_pos_keys_lf.keys())
    dict_lf_settings = {k: parse_lf(os.path.join(path_temp, k), lf_settings, dict_pos_keys_lf) for k in lf_settings}
    return dict_lf_settings


def parse_lf_all_results(path_temp, dict_pos_keys_lf=const.dict_pos_keys_lf_results):
    dict_lf_results = parse_lf_all_settings(path_temp, dict_pos_keys_lf)
    return dict_lf_results


if __name__ == '__main__':
    LFNL4 = parse_lf(r'E:\01_Research\98_Data\华中电网大数据\HZ_t\Temp\LF.NL4')
    path_t = r'E:\01_Research\98_Data\华中电网大数据\HZ_t\Temp'
    path_t = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_LF+ST_SmallSystem_DoubleLine_backup_temp'
    dt_r = parse_lf_all_results(path_t)
    dt = parse_lf_all_settings(path_t)
    print(dt)
