from PyPSASP.constants import const
from PyPSASP.utils.utils_PSASP import reshape_pos_keys

import os


class PSASP_Writer(object):
    def __init__(self, path_temp=''):
        self.__path_temp = path_temp

    def write_to_file(self, file_path, list_dict_values, pos_keys):
        if list_dict_values:
            if isinstance(list_dict_values, dict):
                list_dict_values = [list_dict_values]
            pos_keys_multiline = reshape_pos_keys(pos_keys)
            lines_write = [','.join([str(x[pos_keys_t[hh]]) for hh in range(len(pos_keys_t))]) + ',\n'
                           for pos_keys_t in pos_keys_multiline for x in list_dict_values]
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


