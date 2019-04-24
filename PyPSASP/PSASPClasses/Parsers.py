import math
import re
import os

from PyPSASP.utils import utils_gadgets
from PyPSASP.constants import const

# import numpy as np


class PSASP_Parser(object):
    def __init__(self, path_temp):
        self.__path_temp = path_temp

    def parse_lines_PSASP(self, lines, pos_keys, pattern_parse=const.Pattern_read, multi_line=1, key_busno=None):
        lines_t = lines.copy()
        if str.find(lines_t[0], const.CreatedOnPattern) != -1:
            list.pop(lines_t, 0)

        flag_single_row = False
        if multi_line is True:
            multi_line = len(lines)
            flag_single_row = True

        if multi_line > 1:
            num_lines = len(lines_t)
            Ndiv = math.ceil(num_lines / multi_line)
            lines_t = [','.join([lines_t[hh].strip(',') for hh in range(h * multi_line, (h + 1) * multi_line)]) for h in
                       range(Ndiv)]

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
                        vt = utils_gadgets.convert_s(contents[hh])
                        '''
                        trans_func_t = dict_translate[key_t]
                        if trans_func_t:
                            vt = trans_func_t(contents[hh])
                        else:
                            vt = contents[hh]
                        '''
                        dict_t[key_t] = vt
                    if append_no:
                        dict_t[key_busno] = h + 1
                    list_dict_parsed.append(dict_t)
        if flag_single_row:
            list_dict_parsed = list_dict_parsed[0]
        return list_dict_parsed

    def parse_single_s(self, label_calType, label_getType, label_eleType):
        fnt = const.dict_mapping_files[label_calType][label_getType][label_eleType]
        fpt = os.path.join(self.__path_temp, fnt)
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
                list_dict_parsed = self.parse_lines_PSASP(lines, pos_keys, multi_line=multi_line, key_busno=key_busno)
                return list_dict_parsed

    def parse_single_s_lfs(self, label_eleType):
        return self.parse_single_s(const.LABEL_LF, const.LABEL_SETTINGS, label_eleType)

    def parse_single_s_lfr(self, label_eleType):
        return self.parse_single_s(const.LABEL_LF, const.LABEL_RESULTS, label_eleType)

    def parse_single_s_sts(self, label_eleType):
        return self.parse_single_s(const.LABEL_ST, const.LABEL_SETTINGS, label_eleType)

    def parse_lf(self, lf, pos_keys):
        path_lf = os.path.join(self.__path_temp, lf)
        if os.path.isfile(path_lf):
            with open(path_lf, 'r') as f:
                lines_raw = f.readlines()
            lines = [x.strip() for x in lines_raw]
            if lines:
                if lf in const.dict_multiline.keys():
                    multi_line = const.dict_multiline[lf]
                else:
                    multi_line = 1
                if lf in const.files_lf_append_no:
                    key_busno = const.BusNoKey
                else:
                    key_busno = None

                list_dict_parsed = self.parse_lines_PSASP(lines, pos_keys, multi_line=multi_line, key_busno=key_busno)
                return list_dict_parsed
        else:
            return None

    def parse_all_files_s(self, label_calType, label_getType, label_eles_do=None):
        dict_files = const.dict_mapping_files[label_calType][label_getType]
        # dict_pos_keys = const.dict_mapping_pos_keys[label_calType][label_getType]
        labels_do_ori = list(dict_files.keys())
        flag_single = False
        if label_eles_do is not None:
            if isinstance(label_eles_do, str):
                flag_single = True
                label_eles_do = [label_eles_do]
            label_eles_do = set(labels_do_ori).intersection(set(label_eles_do))
        else:
            label_eles_do = labels_do_ori
        dict_r = {k: self.parse_single_s(label_calType, label_getType, k) for k in label_eles_do}
        if flag_single and len(dict_r) == 1:
            dict_r = list(dict_r.values())[0]
        return dict_r

    def parse_all_settings_lf(self, labels_do=None):
        return self.parse_all_files_s(const.LABEL_LF, const.LABEL_SETTINGS, labels_do)

    def parse_all_results_lf(self, labels_do=None):
        return self.parse_all_files_s(const.LABEL_LF, const.LABEL_RESULTS, labels_do)

    def parse_all_settings_st(self, labels_do=None):
        return self.parse_all_files_s(const.LABEL_ST, const.LABEL_SETTINGS, labels_do)

    def import_STOUT(self, path_STOUT):
        data_STOUT = []
        if os.path.isdir(path_STOUT):
            path_STOUT = os.path.join(path_STOUT, const.FILE_STOUT)
        if os.path.isfile(path_STOUT):
            with open(path_STOUT, 'r') as f:
                data_raw = f.readlines()
            data_STOUT = [[int(xx) for xx in x.strip().split(',') if xx] for x in data_raw]
        return data_STOUT

    def parse_output_st_varinfs(self, path_STOUT=None):
        if path_STOUT is None:
            path_STOUT = self.__path_temp
        list_desc_outputs = []

        data_STOUT = self.import_STOUT(path_STOUT)
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

    def get_output_data_raw(self):
        count_t = 1
        data_FN = []
        while True:
            FNt = os.path.join(self.__path_temp, const.FILE_TEMPLATE_OUTPUT_ST.format(count_t))
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

    # TODO: consider the situation where we enable Lstop (stop simulation instantly at the unstable moment) ?
    def get_sim_time(self):
        dict_conf_ST = self.parse_single_s(const.LABEL_ST, const.LABEL_SETTINGS, const.LABEL_CONF)
        Ttotal = dict_conf_ST[const.STTTotalKey]
        DT = dict_conf_ST[const.STDTKey]
        NT = round(Ttotal / DT) + 1
        list_t = [x * DT for x in range(NT)]
        return list_t

    def parse_output_st(self):
        data_raw = self.get_output_data_raw()
        # data_raw = import_STOUT(path_temp)
        list_desc_outputs = self.parse_output_st_varinfs(self.__path_temp)
        list_t = self.get_sim_time()
        list_heads = [{const.StOutVarNameKey: const.TimeKey},
                      *[dict({const.StOutVarNameKey: const.VarKeyPrefix + str(hh)}, **list_desc_outputs[hh]) for hh in
                        range(len(list_desc_outputs))]]
        list_data_raw_col = [list_t, *data_raw]
        LT = len(list_data_raw_col[0])
        list_data_raw_row = [[x[hh] for x in list_data_raw_col] for hh in range(LT)]
        # list_values = [dict({const.TimeKey:list_t[hh]},**{const.VarKeyPrefix+str(ll):data_raw[ll][hh] for ll in range(len(data_raw))}) for hh in range(len(list_t))]

        return list_heads, list_data_raw_row

    '''
        list_outputs = list_desc_outputs.copy()
        for hh in range(len(list_outputs)):
            list_outputs[hh][const.OutputKeyValues] = data_raw[hh]
        return list_t, list_outputs
    '''

    def write_to_file(self, file_path, list_dict_values, pos_keys):
        if list_dict_values:
            if isinstance(list_dict_values, dict):
                list_dict_values = [list_dict_values]
            lines_write = [','.join([str(x[pos_keys[hh]]) for hh in range(len(pos_keys))]) + ',\n' for x in
                           list_dict_values]
            with open(file_path, 'w') as f:
                f.writelines(lines_write)

    def write_to_file_s(self, label_calType, label_getType, label_eleType, list_dict_values):
        fnt = const.dict_mapping_files[label_calType][label_getType][label_eleType]
        fpt = os.path.join(self.__path_temp, fnt)
        pos_keys_t = const.dict_mapping_pos_keys[label_calType][label_getType][label_eleType]
        self.write_to_file(fpt, list_dict_values, pos_keys_t)
        return fpt

    def write_to_file_s_lfs(self, label_eleType, list_dict_values):
        return self.write_to_file_s(const.LABEL_LF, const.LABEL_SETTINGS, label_eleType, list_dict_values)

    def write_to_file_s_lfs_autofit(self, list_dict_values):
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
            return self.write_to_file_s(const.LABEL_LF, const.LABEL_SETTINGS, label_ele, list_dict_values)


if __name__ == '__main__':
    # path_t = r'E:\01_Research\98_Data\华中电网大数据\华中2016夏（故障卡汇总）\Temp'
    # b = parse_all_results_lf(path_t, const.LABEL_BUS)
    # path_t = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190422_MinInputs'
    path_t = r'E:\05_Resources\Softwares\PSASP\SST\sst_pre'
    Parser_t = PSASP_Parser(path_t)

    path_t_2 = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190419_2'
    from PyPSASP.utils.utils_sqlite import insert_from_list_to_db

    list_heads, list_data = Parser_t.parse_output_st()
    keys_t = [x[const.StOutVarNameKey] for x in list_heads]
    insert_from_list_to_db(r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190419\temp.db',
                           'temp', keys_t, list_data)
    STCAL = Parser_t.parse_single_s(const.LABEL_ST, const.LABEL_RESULTS, const.LABEL_CONF)
    Parser_t_2 = PSASP_Parser(path_t_2)
    t = Parser_t.parse_output_st_varinfs()
    dt = Parser_t.parse_all_settings_lf()
    Parser_t_2.write_to_file_s_lfs_autofit(dt[const.LABEL_GENERATOR])
    list_t, list_outputs = Parser_t.parse_output_st()
    data_FN = Parser_t.get_output_data_raw()
    list_desc_outputs = Parser_t.parse_output_st_varinfs()
    settings_st = Parser_t.parse_all_settings_st()
    dt_r = Parser_t.parse_all_results_lf()
    dt = Parser_t.parse_all_settings_lf()
    print(dt)
