from PyPSASP.utils import utils_sqlite, utils_gadgets
from PyPSASP.PSASPClasses.Parsers import PSASP_Parser
from PyPSASP.PSASPClasses.Converters import PSASP_Converter
from PyPSASP.PSASPClasses.PSASP import OUTPUT_LF_KEY, SUCCESS_LF_KEY, CCT_KEY
from PyPSASP.constants import const
import os
import pickle

path_save = r'F:\Data\Research\PyPSASP\CCT\3m'
path_record_master = os.path.join(path_save, 'record.db')
path_record_master_new = os.path.join(path_save, 'record_master.db')
path_record_master_new_new = os.path.join(path_save, 'record_master_overall.db')
path_record_lf = os.path.join(path_save, 'record_lf.db')



Converter_t = PSASP_Converter()

lfs_brief = utils_sqlite.read_db(path_record_lf,const.CompletedLFTable,return_dict_form=True)
records = utils_sqlite.read_db(path_record_master_new,const.RecordMasterTable,return_dict_form=True)
records_dict = {x[const.TokenKey]:x for x in records}
results = {}
for hh in range(len(lfs_brief)):
#for hh in range(10):
    token_t = lfs_brief[hh][const.TokenKey]
    results[token_t] = {}
    lf_table_t = lfs_brief[hh][OUTPUT_LF_KEY]
    lf_t_list = utils_sqlite.read_db(path_record_lf,lf_table_t,return_dict_form=True)
    lf_t_dict = Converter_t.convert_get2dict(lf_t_list)
    load_flow_t = pickle.dumps(lf_t_dict)
    results[token_t][const.LABEL_LF] = lf_t_dict
    # results[token_t][const.LABEL_LF] = load_flow_t
    if token_t in records_dict.keys():
        results[token_t].update(records_dict[token_t])
    print(hh)

results_list = list(results.values())
utils_sqlite.insert_from_list_to_db(path_record_master_new_new,const.RecordMasterTable,None,results_list,primary_key=const.TokenKey)


S = utils_sqlite.read_db(path_record_master_new_new,const.RecordMasterTable,return_dict_form=True)