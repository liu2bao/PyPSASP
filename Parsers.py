import Gadgets_PSASP
import const
import math
import re
import os


# import numpy as np


def parse_lines_PSASP(lines, pos_keys, dict_translate=const.dict_translate,
                      pattern_parse=const.Pattern_read, multi_line=1, key_busno=None):
    lines_t = lines.copy()
    if str.find(lines_t[0], 'Created on') != -1:
        list.pop(lines_t, 0)

    flag_single_row = False
    if multi_line is True:
        multi_line = len(lines)
        flag_single_row = True

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
    if flag_single_row:
        list_dict_parsed = list_dict_parsed[0]
    return list_dict_parsed


def parse_lf_s(path_temp,label_calType,label_getType,label_eleType):
    fnt = const.dict_mapping_files[label_calType][label_getType][label_eleType]
    fpt = os.path.join(path_temp,fnt)
    if os.path.isfile(fpt):
        with open(fpt, 'r') as f:
            lines_raw = f.readlines()
        lines = [x.strip() for x in lines_raw]
        if lines:
            pos_keys = const.dict_mapping_pos_keys[label_calType][label_getType][label_eleType]
            if fnt in const.dict_multiline.keys():
                multi_line = const.dict_multiline[fnt]
            else:
                multi_line = 1
            if fnt in const.files_lf_append_no:
                key_busno = const.BusNoKey
            else:
                key_busno = None
            list_dict_parsed = parse_lines_PSASP(lines, pos_keys, multi_line=multi_line, key_busno=key_busno)
            return list_dict_parsed


def parse_lf(path_lf, pos_keys):
    suppath_t, lf_t = os.path.split(path_lf)
    if os.path.isfile(path_lf):
        with open(path_lf, 'r') as f:
            lines_raw = f.readlines()
        lines = [x.strip() for x in lines_raw]
        if lines:
            if lf_t in const.dict_multiline.keys():
                multi_line = const.dict_multiline[lf_t]
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



def parse_all_files_s(path_temp, label_calType, label_getType, label_eles_do=None):
    dict_files = const.dict_mapping_files[label_calType][label_getType]
    dict_pos_keys = const.dict_mapping_pos_keys[label_calType][label_getType]
    labels_do_ori = list(dict_files.keys())
    flag_single = False
    if label_eles_do is not None:
        if isinstance(label_eles_do, str):
            flag_single = True
            label_eles_do = [label_eles_do]
        label_eles_do = set(labels_do_ori).intersection(set(label_eles_do))
    else:
        label_eles_do = labels_do_ori
    dict_r = {k: parse_lf_s(path_temp,label_calType,label_getType,k) for k in label_eles_do}
    if flag_single and len(dict_r) == 1:
        dict_r = list(dict_r.values())[0]
    return dict_r


def parse_all_settings_lf(path_temp, labels_do=None):
    return parse_all_files_s(path_temp, const.LABEL_LF, const.LABEL_SETTINGS, labels_do)


def parse_all_results_lf(path_temp, labels_do=None):
    return parse_all_files_s(path_temp, const.LABEL_LF, const.LABEL_RESULTS, labels_do)


def parse_all_settings_st(path_temp, labels_do=None):
    return parse_all_files_s(path_temp, const.LABEL_ST, const.LABEL_SETTINGS, labels_do)


def import_STOUT(path_STOUT):
    data_STOUT = []
    if os.path.isdir(path_STOUT):
        path_STOUT = os.path.join(path_STOUT, const.FILE_STOUT)
    if os.path.isfile(path_STOUT):
        with open(path_STOUT, 'r') as f:
            data_raw = f.readlines()
        data_STOUT = [[int(xx) for xx in x.strip().split(',') if xx] for x in data_raw]
    return data_STOUT


def parse_output_vars(path_STOUT):
    list_desc_outputs = []

    data_STOUT = import_STOUT(path_STOUT)
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
            vec_subtype_t = [0] * num_var_t
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
        if all([x is not None for x in [num_var_t, vec_subtype_t, no_var_t]]):
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
        FNt = os.path.join(path_temp, const.FILE_TEMPLATE_OUTPUT_ST.format(count_t))
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

'''
def parse_conf_legacy(file_path, pos_keys, dict_translate=const.dict_translate_conf):
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
'''


def get_sim_time(path_temp):
    dict_conf_ST = parse_lf_s(path_temp,const.LABEL_ST,const.LABEL_SETTINGS,const.LABEL_CONF)
    Ttotal = dict_conf_ST[const.STTTotalKey]
    DT = dict_conf_ST[const.STDTKey]
    NT = round(Ttotal / DT) + 1
    list_t = [x * DT for x in range(NT)]
    return list_t


def parse_output(path_temp):
    data_raw = get_output_data_raw(path_temp)
    #data_raw = import_STOUT(path_temp)
    list_desc_outputs = parse_output_vars(path_temp)
    list_t = get_sim_time(path_temp)
    list_heads = [{const.ColNameKey:const.TimeKey}, *[dict({const.ColNameKey:const.VarKeyPrefix+str(hh)},**list_desc_outputs[hh]) for hh in range(len(list_desc_outputs))]]
    list_values = [dict({const.TimeKey:list_t[hh]},**{const.VarKeyPrefix+str(ll):data_raw[ll][hh] for ll in range(len(data_raw))}) for hh in range(len(list_t))]

    return list_heads,list_values
'''
    list_outputs = list_desc_outputs.copy()
    for hh in range(len(list_outputs)):
        list_outputs[hh][const.OutputKeyValues] = data_raw[hh]
    return list_t, list_outputs
'''



def write_to_file(file_path, list_dict_values, pos_keys):
    if list_dict_values:
        if isinstance(list_dict_values, dict):
            list_dict_values = [list_dict_values]
        lines_write = [','.join([str(x[pos_keys[hh]]) for hh in range(len(pos_keys))]) + ',\n' for x in
                       list_dict_values]
        with open(file_path, 'w') as f:
            f.writelines(lines_write)


def write_to_file_s(path_temp, label_calType, label_getType, label_eleType, list_dict_values):
    fnt = const.dict_mapping_files[label_calType][label_getType][label_eleType]
    fpt = os.path.join(path_temp, fnt)
    pos_keys_t = const.dict_mapping_pos_keys[label_calType][label_getType][label_eleType]
    write_to_file(fpt, list_dict_values, pos_keys_t)
    return fpt


def write_to_file_s_lfs(path_temp, label_eleType, list_dict_values):
    return write_to_file_s(path_temp, const.LABEL_LF, const.LABEL_SETTINGS, label_eleType, list_dict_values)


def write_to_file_s_lfs_autofit(path_temp, list_dict_values):
    if list_dict_values:
        # TODO: get all posible keys?
        keys_t = set(list_dict_values[0].keys())
        dt = const.dict_pos_keys_lf_settings
        K_overlap = {k: len(keys_t.intersection(set(v))) for k, v in dt.items()}
        MK = max(list(K_overlap.values()))
        labels_posible = [k for k, v in K_overlap.items() if v == MK]
        if len(labels_posible) > 1:
            dL = {k: abs(len(keys_t) - len(v)) for k, v in dt.items() if k in labels_posible}
            mDL = min(list(dL.values()))
            label_ele = [k for k, v in dL.items() if v == mDL][0]
        else:
            label_ele = labels_posible[0]
        return write_to_file_s(path_temp, const.LABEL_LF, const.LABEL_SETTINGS, label_ele, list_dict_values)


if __name__ == '__main__':
    # path_t = r'E:\01_Research\98_Data\华中电网大数据\华中2016夏（故障卡汇总）\Temp'
    # b = parse_all_results_lf(path_t, const.LABEL_BUS)
    path_t = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190419'
    tt = parse_output(path_t)
    t = parse_output_vars(path_t)
    dt = parse_all_settings_lf(path_t)
    write_to_file_s_lfs_autofit('', dt[const.LABEL_GENERATOR])
    list_t, list_outputs = parse_output(path_t)
    data_FN = get_output_data_raw(path_t)
    var_types, var_subtypes, no_desc = parse_output_vars(path_t)
    settings_st = parse_all_settings_st(path_t)
    dt_r = parse_all_results_lf(path_t)
    dt = parse_all_settings_lf(path_t)
    print(dt)
