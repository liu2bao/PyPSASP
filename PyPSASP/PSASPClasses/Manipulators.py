import re
import os
from PyPSASP.utils import utils_gadgets
from PyPSASP.constants import const
from PyPSASP.utils.utils_PSASP import reshape_pos_keys


# import numpy as np

class PSASP_Converter(object):
    def __init__(self):
        pass

    def convert_get2list(self, dict_get):
        list_get = []
        for ele_type, list_ele in dict_get.items():
            if list_ele:
                for hh in range(len(list_ele)):
                    ele = list_ele[hh]
                    list_get_t = [{const.EleTypeKey: ele_type, const.EleIdKey: hh, const.EleAttrNameKey: k,
                                   const.EleAttrValueKey: v} for k, v in ele.items()]
                    list_get.extend(list_get_t)
        return list_get

    def convert_get2dict(self, list_get):
        eleTypes = set([x[const.EleTypeKey] for x in list_get])
        idmax = {k: max([x[const.EleIdKey] for x in list_get if x[const.EleTypeKey] == k]) for k in eleTypes}
        dict_get = {k: [dict()] * (v + 1) for k, v in idmax.items()}
        for get_t in list_get:
            dict_get[get_t[const.EleTypeKey]][get_t[const.EleIdKey]][get_t[const.EleAttrNameKey]] = get_t[
                const.EleAttrValueKey]
        return dict_get



class PSASP_Parser(object):
    def __init__(self, path_temp=''):
        self.__path_temp = path_temp

    def parse_lines_PSASP(self, lines, pos_keys, pattern_parse=const.Pattern_read, key_busno=None):
        lines_t = lines.copy()
        if str.find(lines_t[0], const.CreatedOnPattern) != -1:
            list.pop(lines_t, 0)

        pos_keys_multiline = reshape_pos_keys(pos_keys)
        list_dict_parsed = []
        append_no = isinstance(key_busno, str)
        count_t = 0
        count_num = 0
        dict_t = {}
        for h in range(len(lines_t)):
            line_t = lines_t[h]
            if isinstance(line_t,str):
                line_t = line_t.strip()
                pos_keys_t = pos_keys_multiline[count_t]
                if isinstance(line_t, str):
                    contents = re.findall(pattern_parse, line_t)
                    if not contents and len(pos_keys_t) == 1:
                        contents = [line_t]
                    if contents:
                        dict_t_part = {pos_keys_t[hh]: utils_gadgets.convert_s(contents[hh]) for hh in
                                       range(min([len(contents), len(pos_keys_t)]))}
                        dict_t.update(dict_t_part)
                        if append_no:
                            dict_t[key_busno] = count_num + 1
                count_t += 1
                count_num += 1
                if count_t >= len(pos_keys_multiline):
                    list_dict_parsed.append(dict_t)
                    dict_t = dict()
                    count_t = 0
        return list_dict_parsed

    def parse_single_s(self, label_calType, label_getType, label_eleType):
        fnt = const.dict_mapping_files[label_calType][label_getType][label_eleType]
        fpt = os.path.join(self.__path_temp, fnt)
        if os.path.isfile(fpt):
            with open(fpt, 'r') as f:
                lines_raw = f.readlines()
            lines = [x.strip() for x in lines_raw]
            if lines:
                dmpk = const.dict_mapping_pos_keys
                if label_calType in dmpk.keys():
                    dmpk_sub_1 = dmpk[label_calType]
                    if label_getType in dmpk_sub_1.keys():
                        dmpk_sub_2 = dmpk_sub_1[label_getType]
                        if label_eleType in dmpk_sub_2.keys():
                            pos_keys = dmpk_sub_2[label_eleType]
                            if fnt in const.files_lf_append_no:
                                key_busno = const.BusNoKey
                            else:
                                key_busno = None
                            list_dict_parsed = self.parse_lines_PSASP(lines, pos_keys, key_busno=key_busno)
                            return list_dict_parsed

    def parse_single_s_lfs(self, label_eleType):
        """Parse single file of load flow settings (LF.L*)"""
        return self.parse_single_s(const.LABEL_LF, const.LABEL_SETTINGS, label_eleType)

    def parse_single_s_lfr(self, label_eleType):
        """Parse single file of load flow results (LF.LP*)"""
        return self.parse_single_s(const.LABEL_LF, const.LABEL_RESULTS, label_eleType)

    def parse_single_s_sts(self, label_eleType):
        """Parse single file of transient stability settings (ST.S*)"""
        return self.parse_single_s(const.LABEL_ST, const.LABEL_SETTINGS, label_eleType)

    def parse_single_s_str(self, label_eleType):
        """Parse single file of transient stability results (ST.CAL, STANA.DAT)"""
        return self.parse_single_s(const.LABEL_ST, const.LABEL_RESULTS, label_eleType)

    def parse_all_files_s(self, label_calType, label_getType, label_eles_do=None):
        """Parse all files of a given calculation-type and get-type"""
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

    def parse_all_calType(self,label_calType,labels_getType=None,labels_do=None):
        """Parse all files of a given calculation-type"""
        if labels_getType is None:
            lgt = tuple(const.dict_mapping_pos_keys.keys())
        else:
            lgt = tuple(set(labels_getType).intersection(const.dict_mapping_pos_keys[label_calType].keys()))
        dict_t = {k:self.parse_all_files_s(label_calType,k,labels_do) for k in lgt}
        return dict_t

    def parse_all_lf_sr(self,labels_getType=None,labels_do=None):
        """Parse all load flow files of given get-types"""
        return self.parse_all_calType(const.LABEL_LF,labels_getType,labels_do)

    def parse_all_lf(self, label_getType, labels_do=None):
        """Parse all load flow files of a given get-types"""
        return self.parse_all_files_s(const.LABEL_LF, label_getType, labels_do)

    def parse_all_settings_lf(self, labels_do=None):
        """Parse all setting files of load flow"""
        return self.parse_all_lf(const.LABEL_SETTINGS, labels_do)

    def parse_all_results_lf(self, labels_do=None):
        """Parse all result files of load flow"""
        return self.parse_all_lf(const.LABEL_RESULTS, labels_do)

    def parse_all_settings_st(self, labels_do=None):
        """arse all setting files of transient stability"""
        return self.parse_all_files_s(const.LABEL_ST, const.LABEL_SETTINGS, labels_do)

    def parse_output_st_varinfs(self, path_STOUT=None):
        """Parse output meanings of transient stability"""
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

    # TODO: consider the situation where we enable Lstop (stop simulation instantly at the unstable moment) ?
    def get_sim_time(self):
        dict_conf_ST = self.parse_single_s(const.LABEL_ST, const.LABEL_SETTINGS, const.LABEL_CONF)[0]
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


    def get_gen_angles_st(self):
        list_heads, list_data_raw_row = self.parse_output_st()
        idx_gen_angle = [hh for hh in range(len(list_heads)) if (const.OutputKeyType in list_heads[hh].keys()) and (list_heads[hh][const.OutputKeyType] == 1)]
        gen_angles = [list_data_raw_row[hhh] for hhh in idx_gen_angle]
        return gen_angles

    def parse_all_parsable(self):
        dict_parsable_all = {}
        for label_calType, dict_files_sub_1 in const.dict_mapping_files.items():
            dict_parsable_all[label_calType] = {}
            for label_getType, dict_files_sub_2 in dict_files_sub_1.items():
                dict_parsable_all[label_calType][label_getType] = {}
                for label_eleType, dict_files_sub_3 in dict_files_sub_2.items():
                    dt = self.parse_single_s(label_calType, label_getType, label_eleType)
                    if dt:
                        dict_parsable_all[label_calType][label_getType][label_eleType] =  dt
        return dict_parsable_all


    def import_STOUT(self, path_STOUT):
        data_STOUT = []
        if os.path.isdir(path_STOUT):
            path_STOUT = os.path.join(path_STOUT, const.FILE_STOUT)
        if os.path.isfile(path_STOUT):
            with open(path_STOUT, 'r') as f:
                data_raw = f.readlines()
            data_STOUT = [[int(xx) for xx in x.strip().split(',') if xx] for x in data_raw]
        return data_STOUT



class PSASP_Writer(object):
    def __init__(self, path_temp=''):
        self.__path_temp = path_temp

    def write_to_file(self, file_path, list_dict_values, pos_keys):

        suppath,fnt = os.path.split(file_path)
        if not os.path.isdir(suppath):
            os.makedirs(suppath)

        if list_dict_values:
            if isinstance(list_dict_values, dict):
                list_dict_values = [list_dict_values]
            pos_keys_multiline = reshape_pos_keys(pos_keys)
            lines_write = [(','.join(
                [str(x[pos_keys_t[hh]]) for hh in range(len(pos_keys_t)) if pos_keys_t[hh] in x.keys()]) + ',\n')
                           for x in list_dict_values if x for pos_keys_t in pos_keys_multiline]
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
            # TODO: get all possible keys?
            keys_t = set(list_dict_values[0].keys())
            dt = const.dict_pos_keys_lf_settings
            K_overlap = {k: len(keys_t.intersection(set(utils_gadgets.cat_lists(v) if isinstance(v[0],list) else v))) for k, v in dt.items()}
            MK = max(list(K_overlap.values()))
            labels_posible = [k for k, v in K_overlap.items() if v == MK]
            if len(labels_posible) > 1:
                dL = {k: abs(len(keys_t) - len(v)) for k, v in dt.items() if k in labels_posible}
                mDL = min(list(dL.values()))
                label_ele = [k for k, v in dL.items() if v == mDL][0]
            else:
                label_ele = labels_posible[0]
            return self.write_to_file_s(const.LABEL_LF, const.LABEL_SETTINGS, label_ele, list_dict_values)

    def write_all_writable(self,dict_all):
        for label_calType,dict_files_sub_1 in dict_all.items():
            for label_getType,dict_files_sub_2 in dict_files_sub_1.items():
                for label_eleType,dict_files_sub_3 in dict_files_sub_2.items():
                    lt = dict_all[label_calType][label_getType][label_eleType]
                    self.write_to_file_s(label_calType,label_getType,label_eleType,lt)


if __name__ == '__main__':
    path_temp = r'E:\01_Research\98_Data\SmallSystem_PSASP\SMIB\SMIB_0'
    Parser_t = PSASP_Parser(path_temp)
    list_heads,list_output = Parser_t.parse_output_st()
    pass