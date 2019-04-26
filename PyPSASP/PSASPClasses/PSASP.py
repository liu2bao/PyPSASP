import os
from PyPSASP.utils.utils_PSASP import copyfiles_st, copyfiles_lf, copyfiles_lfs
from PyPSASP.utils.utils_gadgets import generate_new_files_save_yield, gen_token, formulate_list_of_dicts
from PyPSASP.utils.utils_sqlite import insert_from_list_to_db
from PyPSASP.constants import const
from PyPSASP.PSASPClasses.Executors import executor_PSASP_lf, executor_PSASP_st
from PyPSASP.PSASPClasses.Executors import executor_PSASP_sstlin, executor_PSASP_ssteig
from PyPSASP.PSASPClasses.Parsers import PSASP_Parser, PSASP_Converter
import random
import pickle

PATH_TEMP = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190419'
PATH_RESOURCES = r'E:\05_Resources\Softwares\PSASP\CriticalFiles_60000'
PATH_OUTPUT = r'F:\Data\Research\PyPSASP\CCT\3m'

OUTPUT_LF_KEY = 'output_lf'
SUCCESS_LF_KEY = 'success_lf'
CCT_KEY = 'CCT'

def func_change_lf_temp(P):
    if isinstance(P, PSASP):
        gen_ori = P.parser.parse_single_s_lfs(const.LABEL_GENERATOR)
        load_ori = P.parser.parse_single_s_lfs(const.LABEL_LOAD)
        gen_new = gen_ori.copy()
        load_new = load_ori.copy()
        Psum = 0
        for hh in range(len(gen_new)):
            gen_new[hh][const.GenPgKey] = gen_new[hh][const.PmaxKey] * (random.random() * 0.5 + 0.5)
            gen_new[hh][const.V0Key] = (random.random() * 0.2 + 0.95)
            Psum = Psum + gen_new[hh][const.GenPgKey]
            '''
            for key_t in [const.GenPgKey,const.GenQgKey,const.V0Key,const.AngleKey]:
                gen_new[hh][key_t] = gen_new[hh][key_t]*(random.random()*0.5+0.5)
            '''
        rands_t = [random.random() for hh in range(len(load_new))]
        Ap = random.random() * 0.4 + 0.8
        Pls_t = [x / sum(rands_t) * Ap * Psum for x in rands_t]
        for hh in range(len(load_new)):
            load_new[hh][const.LoadPlKey] = Pls_t[hh]
            load_new[hh][const.LoadQlKey] = 6 * random.random()
            '''
            for key_t in [const.LoadPlKey,const.LoadQlKey,const.V0Key,const.AngleKey]:
                load_new[hh][key_t] = load_new[hh][key_t]*(random.random()*0.5+0.5)
            '''

        P.parser.write_to_file_s_lfs_autofit(gen_new)
        P.parser.write_to_file_s_lfs_autofit(load_new)


def func_change_t_regular(P, t):
    if isinstance(P, PSASP):
        STS11_ori = P.parser.parse_single_s(const.LABEL_ST, const.LABEL_SETTINGS, const.LABEL_FAULT)
        STS11_new = STS11_ori.copy()
        STS11_new[0][const.FaultTstartKey] = 0
        STS11_new[1][const.FaultTstartKey] = t
        STS11_new[2][const.FaultTstartKey] = t + 0.01
        P.parser.write_to_file_s(const.LABEL_ST, const.LABEL_SETTINGS, const.LABEL_FAULT, STS11_new)


def func_judge_stable_regular(P):
    F = None
    if isinstance(P, PSASP):
        STCAL = P.parser.parse_single_s(const.LABEL_ST, const.LABEL_RESULTS, const.LABEL_CONF)
        F = STCAL[const.STIsStableKey] == 1
    return F


class PSASP(object):
    @property
    def path_temp(self):
        return self.__path_temp

    @property
    def path_resources(self):
        return self.__path_resources

    @path_temp.setter
    def path_temp(self, value):
        if not isinstance(value, str):
            raise ValueError('path_temp must be a string!')
        elif not os.path.isdir(value):
            os.makedirs(value)
        self.__path_temp = value
        self.parser = PSASP_Parser(value)
        self.converter = PSASP_Converter()

    @path_resources.setter
    def path_resources(self, value):
        if not isinstance(value, str):
            raise ValueError('path_resources must be a string!')
        elif not os.path.isdir(value):
            raise ValueError('path_resources should be an existing folder!')
        self.__path_resources = value
        self.__path_exe_wmlfmsg = os.path.join(self.__path_resources, const.EXE_LF)
        self.__path_exe_wmudrt = os.path.join(self.__path_resources, const.EXE_ST)
        self.__path_exe_wsstlin = os.path.join(self.__path_resources, const.EXE_SST_LIN)
        self.__path_exe_wssteig = os.path.join(self.__path_resources, const.EXE_SST_EIG)
        self.__executor_lf = executor_PSASP_lf(self.__path_exe_wmlfmsg, self.path_temp)
        self.__executor_st = executor_PSASP_st(self.__path_exe_wmudrt, self.path_temp)
        self.__executor_sstlin = executor_PSASP_sstlin(self.__path_exe_wsstlin, self.path_temp)
        self.__executor_ssteig = executor_PSASP_ssteig(self.__path_exe_wssteig, self.path_temp)

    def __init__(self, path_temp, path_resources):
        self.path_temp = path_temp
        self.path_resources = path_resources

    def calculate_LF(self):
        success_lf = False
        self.__executor_lf.execute_exe()
        LFCAL = self.parser.parse_single_s(const.LABEL_LF, const.LABEL_RESULTS, const.LABEL_CONF)
        if LFCAL:
            LFCAL = LFCAL[0]
            if const.MCalKey in LFCAL.keys():
                success_lf = LFCAL[const.MCalKey] == 1
        return success_lf

    def calculate_ST(self):
        success_st = False
        self.__executor_st.execute_exe()
        STCAL = self.parser.parse_single_s(const.LABEL_ST, const.LABEL_RESULTS, const.LABEL_CONF)
        if STCAL:
            STCAL = STCAL[0]
            if const.MCalKey in STCAL.keys():
                success_st = STCAL[const.MCalKey] == 1
        return success_st

    # TODO: read CAL file?
    def calculate_SST_LIN(self):
        success_sst_lin = True
        self.__executor_sstlin.execute_exe()
        return success_sst_lin

    # TODO: read CAL file?
    def calculate_SST_EIG(self):
        success_sst_eig = True
        self.__executor_ssteig.execute_exe()
        return success_sst_eig

    def calculate_CCT(self, path_save_left, path_save_right,
                      func_change_t=func_change_t_regular,
                      func_judge_stable=func_judge_stable_regular,
                      Tstep_max=0.2, label=None):

        if label is None:
            label = '-------AFFAIR-------'
        rec = {
            'Tmax': Tstep_max,
            'Tsim': 5,
            'eps': 0.001,
            'tleft': 0,
            'tright': Tstep_max,
            CCT_KEY: float('nan'),
            'fleft': False,
            'fright': True,
            'count': 0,
            'flag_limit_touched': False,
            'output_st_left': path_save_left,
            'output_st_right': path_save_right
        }

        while abs(rec['tleft'] - rec['tright']) > rec['eps']:
            if rec['count'] == 0 or (not rec['flag_limit_touched']):
                CT_t = rec['tright']
            else:
                CT_t = (rec['tleft'] + rec['tright']) / 2
            func_change_t(self, CT_t)
            self.__executor_st.execute_exe()
            stable = func_judge_stable(self)
            if stable:
                rec['tleft'] = CT_t
                rec['fleft'] = stable
                rec[CCT_KEY] = CT_t
                # TODO: Donnot copy?
                copyfiles_st(self.path_temp, rec['output_st_left'])
                if not rec['flag_limit_touched']:
                    rec['tright'] = CT_t + Tstep_max

            else:
                rec['tright'] = CT_t
                rec['fright'] = stable
                # TODO: Donnot copy?
                copyfiles_st(self.path_temp, rec['output_st_right'])
                rec['flag_limit_touched'] = True

            rec['count'] += 1
            print('%s%d (%d): %.4f, %.4f' % (label, rec['count'], stable, rec['tleft'], rec['tright']))
        print('%sCCT = %.4f' % (label, rec[CCT_KEY]))

        return rec


class CCT_generator(object):
    @property
    def path_output(self):
        return self.__path_output

    @path_output.setter
    def path_output(self, value):
        if not isinstance(value, str):
            raise ValueError('path_output should be string!')
        else:
            if not os.path.isdir(value):
                os.makedirs(value)
            self.__path_output = value
            self.__path_record_master = os.path.join(value, 'record_master.db')
            self.__path_record_lf = os.path.join(value, 'record_lf.db')
            self.__path_output_st = os.path.join(value, const.LABEL_ST)
            self.__path_output_st_left = os.path.join(self.__path_output_st, 'left')
            self.__path_output_st_right = os.path.join(self.__path_output_st, 'right')

    def __init__(self, path_temp, path_resources, path_output, func_change_lfs):
        self.__path_temp = path_temp
        self.__PSASP = PSASP(path_temp, path_resources)
        self.path_output = path_output
        self.__func_change_lfs = func_change_lfs
        self.__name_gen_st_left = generate_new_files_save_yield(self.__path_output_st_left, 'left',
                                                                flag_dir=True, return_path=True)
        self.__name_gen_st_right = generate_new_files_save_yield(self.__path_output_st_right, 'right',
                                                                 flag_dir=True, return_path=True)

    def insert_lf_into_db(self, token, table_name, label_sr, lf_t):
        Converter_t = self.__PSASP.converter
        list_lf_t = Converter_t.convert_get2list(lf_t)
        heads, values = formulate_list_of_dicts(list_lf_t)
        insert_from_list_to_db(self.__path_record_lf, table_name, heads, values)
        insert_from_list_to_db(self.__path_record_lf, const.CompletedLFTable,
                               [const.TokenKey, OUTPUT_LF_KEY, const.GetTypeKey], [[token, table_name, label_sr]],
                               primary_key=const.TokenKey)

    def run_sim_CCT_once(self,dump_lf=True):
        self.__func_change_lfs(self.__PSASP)
        success_lf = self.__PSASP.calculate_LF()
        # success_lf = True
        rec_t = {SUCCESS_LF_KEY: success_lf}
        token_t = gen_token()
        rec_t[const.TokenKey] = token_t
        flft = 'lf_' + token_t
        if success_lf:
            fstleftt = next(self.__name_gen_st_left)
            fstrightt = next(self.__name_gen_st_right)
            rec_t_st = self.__PSASP.calculate_CCT(fstleftt, fstrightt)
            rec_t.update(rec_t_st)
            label_t = const.LABEL_RESULTS
        else:
            label_t = const.LABEL_SETTINGS

        Parser_t = self.__PSASP.parser
        lf_t = Parser_t.parse_all_files_s(const.LABEL_LF, label_t)
        if dump_lf:
            flft = None
            lf_save_t = pickle.dumps(lf_t)
        else:
            lf_save_t = None
            self.insert_lf_into_db(token_t, flft, label_t, lf_t)
        rec_t[OUTPUT_LF_KEY] = flft
        rec_t[const.LABEL_LF] = lf_save_t
        keys_t = list(rec_t.keys())
        values_t = list(rec_t.values())
        insert_from_list_to_db(self.__path_record_master, const.RecordMasterTable, keys_t, [values_t],
                               primary_key=const.TokenKey)


if __name__ == '__main__':

    os.system('@echo off')
    Cc = CCT_generator(PATH_TEMP, PATH_RESOURCES, PATH_OUTPUT, func_change_lf_temp)
    count_t = 0
    max_count = 10000
    while count_t <= max_count:
        Cc.run_sim_CCT_once()
        count_t += 1

    '''
    path_save = 'save'
    Pt_writer = PSASP(path_save,PATH_TEMP)
    Pt = PSASP(PATH_TEMP,PATH_TEMP)
    Pt.calculate_LF()
    Pt.calculate_ST()
    Pt.calculate_SST_LIN()
    Pt.calculate_SST_EIG()
    G = Pt.parser.parse_single_s(const.LABEL_LF,const.LABEL_SETTINGS,const.LABEL_GENERATOR)
    G_new = G
    # modify G_new
    Pt.parser.write_to_file_s(const.LABEL_LF,const.LABEL_SETTINGS,const.LABEL_GENERATOR,G_new)
    Pt.parser.write_to_file_s_lfs_autofit(G_new)
    f = Pt.calculate_LF()
    if f:
        A = Pt.parser.parse_all_results_lf()
        R = Pt.parser.parse_all_results_lf((const.LABEL_BUS,const.LABEL_GENERATOR))
        evalue = Pt.parser.parse_single_s(const.LABEL_SST_EIG,const.LABEL_RESULTS,const.LABEL_EIGVAL)

        evec = Pt.parser.parse_single_s(const.LABEL_SST_EIG,const.LABEL_RESULTS,const.LABEL_EIGVEC)
    
    '''
