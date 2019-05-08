from PyPSASP.constants import const
from PyPSASP.utils.utils_PSASP import reshape_pos_keys

import os


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

    # TODO: this is not right for LF.L1 and ST.S1
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

    def write_all_writable(self,dict_all):
        for label_calType,dict_files_sub_1 in dict_all.items():
            for label_getType,dict_files_sub_2 in dict_files_sub_1.items():
                for label_eleType,dict_files_sub_3 in dict_files_sub_2.items():
                    lt = dict_all[label_calType][label_getType][label_eleType]
                    self.write_to_file_s(label_calType,label_getType,label_eleType,lt)



if __name__=='__main__':
    from PyPSASP.PSASPClasses.Parsers import PSASP_Parser
    path_temp = r'E:\01_Research\98_Data\SmallSystem_PSASP\SMIB\2016_06_01T00_00_24'
    path_temp_2 = r'E:\01_Research\98_Data\SmallSystem_PSASP\SMIB\2016_06_01T00_00_24_copy'
    Parser_t = PSASP_Parser(path_temp)
    Writer_t = PSASP_Writer(path_temp_2)
    T = Parser_t.parse_all_parsable()
    Writer_t.write_all_writable(T)


