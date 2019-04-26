from PyPSASP.utils import utils_sqlite, utils_gadgets
from PyPSASP.PSASPClasses.Parsers import PSASP_Parser, PSASP_Converter
from PyPSASP.PSASPClasses.PSASP import OUTPUT_LF_KEY, SUCCESS_LF_KEY
from PyPSASP.constants import const
import os

path_save = r'F:\Data\Research\PyPSASP\CCT\3m'
path_record_master = os.path.join(path_save, 'record.db')
path_record_master_new = os.path.join(path_save, 'record_master.db')
path_record_lf = os.path.join(path_save, 'record_lf.db')
Converter_t = PSASP_Converter()


TT_e = utils_sqlite.read_db(path_record_lf, const.CompletedLFTable, return_dict_form=True)
paths_lf_e = [t[OUTPUT_LF_KEY] for t in TT_e]
T = utils_sqlite.read_db(path_record_master, const.RecordMasterTable, return_dict_form=True)
TT = []
for hh in range(len(T)):
    tt = T[hh].copy()
    path_lf_t = T[hh][OUTPUT_LF_KEY]
    if path_lf_t in paths_lf_e:
        continue
    token_t = utils_gadgets.gen_token()
    tt[const.TokenKey] = token_t
    success_lf_t = T[hh][SUCCESS_LF_KEY]
    Parser_t = PSASP_Parser(path_lf_t)
    if success_lf_t:
        label_t = const.LABEL_RESULTS
    else:
        label_t = const.LABEL_SETTINGS
    lft = Parser_t.parse_all_lf(label_t)
    list_lft = Converter_t.convert_get2list(lft)
    heads, values = utils_gadgets.formulate_list_of_dicts(list_lft)
    lf_table_t = 'lf_' + token_t
    tt[OUTPUT_LF_KEY] = lf_table_t
    utils_sqlite.insert_from_list_to_db(path_record_lf, lf_table_t, heads, values)
    utils_sqlite.insert_from_list_to_db(path_record_lf, const.CompletedLFTable,
                                        [const.TokenKey, OUTPUT_LF_KEY, const.GetTypeKey],
                                        [[token_t, lf_table_t, label_t]],
                                        primary_key=const.TokenKey)
    TT.append(tt)

keys_t, values_t = utils_gadgets.formulate_list_of_dicts(TT)
utils_sqlite.insert_from_list_to_db(path_record_master_new, const.RecordMasterTable, keys_t, values_t,
                                    primary_key=const.TokenKey)
