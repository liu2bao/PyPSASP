import Gadgets_PSASP
import const
import math
import re
import os
from numpy import linspace

# import numpy as np


def parse_lines_PSASP(lines, pos_keys, dict_translate=const.dict_translate_files,
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
                    dict_t[key_busno] = h + 1
                list_dict_parsed.append(dict_t)

    return list_dict_parsed


def parse_lf(path_lf, pos_keys):
    suppath_t, lf_t = os.path.split(path_lf)
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

            list_dict_parsed = parse_lines_PSASP(lines, pos_keys, multi_line=multi_line, key_busno=key_busno)
            return list_dict_parsed
    else:
        return None


def parse_all_files(path_temp, dict_files, dict_pos_keys, labels_do=None):
    labels_do_ori = list(dict_files.keys())
    flag_single = False
    if labels_do is not None:
        if isinstance(labels_do, str):
            flag_single = True
            labels_do = [labels_do]
        labels_do = set(labels_do_ori).intersection(set(labels_do))
    else:
        labels_do = labels_do_ori
    dict_r = {k: parse_lf(os.path.join(path_temp, dict_files[k]), dict_pos_keys[k]) for k in labels_do}
    if flag_single and len(dict_r) == 1:
        dict_r = list(dict_r.values())[0]
    return dict_r


def parse_all_files_s(path_temp, label_calType, label_eleType, labels_do=None):
    dict_files = const.dict_mapping_files[label_calType][label_eleType]
    dict_pos_keys = const.dict_mapping_pos_keys[label_calType][label_eleType]
    dict_r = parse_all_files(path_temp, dict_files, dict_pos_keys, labels_do)
    return dict_r


def parse_all_settings_lf(path_temp, labels_do=None):
    return parse_all_files_s(path_temp, const.LABEL_LF, const.LABEL_SETTINGS, labels_do)


def parse_all_results_lf(path_temp, labels_do=None):
    return parse_all_files_s(path_temp, const.LABEL_LF, const.LABEL_RESULTS, labels_do)


def parse_all_settings_st(path_temp, labels_do=None):
    return parse_all_files_s(path_temp, const.LABEL_ST, const.LABEL_SETTINGS, labels_do)


def parse_output_vars(path_STOUT):
    list_desc_outputs = []
    if os.path.isdir(path_STOUT):
        path_STOUT = os.path.join(path_STOUT,const.FILE_STOUT)
    if os.path.isfile(path_STOUT):
        with open(path_STOUT, 'r') as f:
            data_raw = f.readlines()
        data_STOUT = [[int(xx) for xx in x.strip().split(',') if xx] for x in data_raw]
        type_t = 0
        for hh in range(len(data_STOUT)):
            data_piece = data_STOUT[hh]
            num_var_t = None
            vec_subtype_t = None
            no_var_t = None
            if data_piece[0] == 0:
                continue
            typett = data_piece[1]
            if typett in [8, 11]:
                continue
            if typett != 99:
                type_t = typett
            if type_t in [1, 2, 12]:
                if type_t in [1, 12]:
                    num_pu = 2
                else:
                    num_pu = 1
                vec_no_t = [x for x in data_piece[2:] if x != 0]
                num_var_t = round(len(vec_no_t) / num_pu)
                no_var_t = [[vec_no_t[ii * num_pu + jj] for jj in range(num_pu)] for ii in range(num_var_t)]
                vec_subtype_t = [0]*num_var_t
            elif type_t in [3, 4, 5, 6, 7, 13, 14]:
                if type_t in [3, 5]:
                    point_start_t = 3
                elif type_t in [6, 7, 13]:
                    point_start_t = 5
                else:
                    point_start_t = 4
                # num_no_t = point_start_t-2
                vec_subtype_t = [x for x in data_piece[point_start_t:] if x != 0]
                num_var_t = len(vec_subtype_t)
                vec_no_t = data_piece[2:point_start_t]
                no_var_t = [vec_no_t] * num_var_t
            if all([x is not None for x in [num_var_t,vec_subtype_t,no_var_t]]):
                for hh in range(num_var_t):
                    dict_t = {}
                    dict_t[const.OutputKeyType] = type_t
                    dict_t[const.OutputKeySubType] = vec_subtype_t[hh]
                    dict_t[const.OutputKeyNoDesc] = no_var_t[hh]
                    list_desc_outputs.append(dict_t)
    return list_desc_outputs


def get_output_data_raw(path_temp):
    count_t = 1
    data_FN = []
    while True:
        FNt = os.path.join(path_temp,const.FILE_TEMPLATE_OUTPUT_ST.format(count_t))
        if os.path.isfile(FNt):
            with open(FNt, 'r') as f:
                data_raw = f.readlines()
            data_FN_rowwise_t = [[float(xx) for xx in x.strip().split(',') if xx] for x in data_raw]
            data_FN_colwise_t = [[k[hh] for k in data_FN_rowwise_t] for hh in range(len(data_FN_rowwise_t[0]))]
            data_FN.extend(data_FN_colwise_t)
            count_t += 1
        else:
            break
    return data_FN


def parse_conf(file_path, pos_keys, dict_translate=const.dict_translate_conf):
    dict_conf = {}
    if os.path.isdir(file_path):
        file_path = os.path.join(file_path, const.FILE_ST_CONF)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            d = f.read()
        contents = d.split(',')
        for hh in range(len(pos_keys)):
            key_t = pos_keys[hh]
            vart = contents[hh]
            funct = dict_translate[key_t]
            if funct:
                vart_new = funct(vart)
            else:
                vart_new = vart
            dict_conf[key_t] = vart_new
    return dict_conf

def parse_conf_s(path_temp,label_calType,dict_translate=const.dict_translate_conf):
    file_path_t = os.path.join(path_temp, const.dict_files_conf[label_calType])
    pos_keys_t = const.dict_pos_keys_conf[label_calType]
    return parse_conf(file_path_t, pos_keys_t,dict_translate)

def parse_conf_LF(path_temp):
    return parse_conf_s(path_temp,const.LABEL_LF)

def parse_conf_ST(path_temp):
    return parse_conf_s(path_temp,const.LABEL_ST)

def get_sim_time(path_temp):
    dict_conf_ST = parse_conf_ST(path_temp)
    Ttotal = dict_conf_ST[const.STTTotalKey]
    DT = dict_conf_ST[const.STDTKey]
    NT = round(Ttotal/DT)+1
    list_t = [x*DT for x in range(NT)]
    return list_t

def parse_output(path_temp):
    data_raw = get_output_data_raw(path_temp)
    list_desc_outputs = parse_output_vars(path_temp)
    list_outputs = list_desc_outputs.copy()
    for hh in range(len(list_outputs)):
        list_outputs[hh][const.OutputKeyValues] = data_raw[hh]
    list_t = get_sim_time(path_temp)
    return list_t,list_outputs



if __name__ == '__main__':
    # path_t = r'E:\01_Research\98_Data\华中电网大数据\华中2016夏（故障卡汇总）\Temp'
    # b = parse_all_results_lf(path_t, const.LABEL_BUS)
    path_t = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190419'
    list_t, list_outputs = parse_output(path_t)
    data_FN = get_output_data_raw(path_t)
    var_types, var_subtypes, no_desc = parse_output_vars(path_t)
    settings_st = parse_all_settings_st(path_t)
    dt_r = parse_all_results_lf(path_t)
    dt = parse_all_settings_lf(path_t)
    print(dt)
