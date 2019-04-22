import os
import const
from Executors import executor_PSASP_lf, executor_PSASP_st


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

    @path_resources.setter
    def path_resources(self, value):
        if not isinstance(value, str):
            raise ValueError('path_resources must be a string!')
        elif not os.path.isdir(value):
            raise ValueError('path_resources should be an existing folder!')
        self.__path_resources = value
        self.__path_exe_wmlfmsg = os.path.join(self.__path_resources, const.EXE_LF)
        self.__path_exe_wmudrt = os.path.join(self.__path_resources, const.EXE_ST)
        self.__executor_lf = executor_PSASP_lf(self.__path_exe_wmlfmsg, self.path_temp)
        self.__executor_st = executor_PSASP_st(self.__path_exe_wmudrt, self.path_temp)

    def __init__(self, path_temp, path_resources):
        self.path_temp = path_temp
        self.path_resources = path_resources

    def calculate_LF(self):
        self.__executor_lf.execute_exe()

    def calculate_CCT(self,func_change_t,func_judge_stable,Tstep_max = 0.2):

        rec = {
            'Tmax': Tstep_max,
            'Tsim': 5,
            'eps': 0.001,
            'tleft': 0,
            'tright': Tstep_max,
            'CCT': float('nan'),
            'fleft': False,
            'fright': True,
            'count': 0,
            'flag_limit_touched': False,
            'output_left': None,
            'output_right': None
        }

        while abs(rec['tleft'] - rec['tright']) > rec['eps']:
            if rec['count'] == 0 or (not rec['flag_limit_touched']):
                CT_t = rec['tright']
            else:
                CT_t = (rec['tleft'] + rec['tright']) / 2
            func_change_t(self,CT_t)
            self.__executor_st.execute_exe()
            stable = func_judge_stable(self)
            if stable:
                rec['tleft'] = CT_t
                rec['fleft'] = stable
                rec['CCT'] = CT_t
                rec['output_left'] =
                if not rec['flag_limit_touched']:
                    rec['tright'] = CT_t + Tstep_max

            else:
                rec['tright'] = CT_t
                rec['fright'] = stable
                oRecord_t_right = copy.deepcopy(oRecord_t)
                rec['flag_limit_touched'] = True

            rec['count'] += 1
            print('%s%d (%d): %.4f, %.4f' % (label, rec['count'], stable, rec['tleft'], rec['tright']))
        print('%sCCT = %.4f' % (label, rec['CCT']))
        if oRecord_t_left:
            oRecord_t_left.write_output(output_file_left)
        if oRecord_t_right:
            oRecord_t_right.write_output(output_file_right)

        return rec
