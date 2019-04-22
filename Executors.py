import psutil
import os
from threading import Thread, Lock
import time
import traceback
import const

TempBat = 'temp.bat'
Lock_GetProcess = Lock()
Lock_WriteBat = Lock()

class executor_PSASP(object):
    def __init__(self, path_exe, path_env=None, path_flagfile=None):
        if isinstance(path_flagfile, str):
            path_t, flag_t = os.path.split(path_flagfile)
            if not path_t:
                path_flagfile = os.path.join(path_env, path_flagfile)
        if not os.path.isfile(path_exe):
            path_t, exe_t = os.path.split(path_exe)
            path_exe = os.path.join(path_env, exe_t)
            if not os.path.isfile(path_exe):
                raise ValueError('%s not exist' % path_exe)
        self.__path_exe = path_exe
        self.__path_env = path_env
        self.__path_flagfile = path_flagfile
        self.__current_process = []
        self.__process_inc_matched = []
        self.__flagfile_last_update_time = None

    def __update_process(self):
        self.__current_process = get_all_process()

    def __get_process_inc(self):
        process_new = get_all_process()
        pid_old = [x['pid'] for x in self.__current_process]
        process_inc = [x for x in process_new if x['pid'] not in pid_old]
        return process_inc

    def __get_process_inc_matched(self, wait_time=0.5, max_try=10):
        process_inc_matched = []
        count = 0
        while count <= max_try:
            process_inc = self.__get_process_inc()
            process_inc_matched = [x for x in process_inc if x['exe'] == self.__path_exe]
            if not process_inc_matched:
                time.sleep(wait_time)
            else:
                break
            count += 1
        return process_inc_matched

    def __update_mtime_flagfile(self):
        self.__flagfile_last_update_time = get_updated_time(self.__path_flagfile)

    def __kill_process_while_flag(self, wait_time=2, max_try=60):
        count = 0
        while get_updated_time(self.__path_flagfile) <= self.__flagfile_last_update_time and count <= max_try:
            time.sleep(wait_time)
            count += 1
        if count >= max_try:
            print('maximum try reached')
        for process_t in self.__process_inc_matched:
            os.system(r'taskkill /pid %d -t -f' % process_t['pid'])
            # print('process killed')

    def execute_exe(self):
        if self.__path_env:
            idx_drive_t = str.find(self.__path_env, ':')
            if idx_drive_t == -1:
                raise ValueError('Drive not found')
            drive_t = self.__path_env[:idx_drive_t + 1]
            if Lock_WriteBat.acquire():
                with open(TempBat, 'w') as f:
                    f.write('%s\n' % drive_t)
                    f.write('cd "%s"\n' % self.__path_env)
                    f.write('"%s"' % self.__path_exe)
            exe_t = TempBat
        else:
            exe_t = self.__path_exe
        if not self.__path_flagfile:
            r = os.system(exe_t)
            return r
        else:
            thread_exe = Thread(target=os.system, args=(exe_t,))
            thread_kill = Thread(target=self.__kill_process_while_flag)
            if Lock_GetProcess.acquire():
                self.__update_process()
                self.__update_mtime_flagfile()
                thread_exe.start()
                self.__process_inc_matched = self.__get_process_inc_matched()
                Lock_GetProcess.release()
            Lock_WriteBat.release()
            thread_kill.start()
            thread_kill.join()
            thread_exe.join()


class executor_PSASP_lf(executor_PSASP):
    def __init__(self,path_exe,path_env):
        executor_PSASP.__init__(self,path_exe,path_env)


class executor_PSASP_st(executor_PSASP):
    def __init__(self,path_exe,path_env):
        flag_file_st = const.dict_mapping_files[const.LABEL_ST][const.LABEL_RESULTS][const.LABEL_CONF]
        executor_PSASP.__init__(self, path_exe, path_env, flag_file_st)


def get_all_process():
    attrs_as_dict = ['pid', 'name', 'username', 'exe', 'create_time']
    pid_list = psutil.pids()
    list_process = []
    for pid in pid_list:
        try:
            dict_t = psutil.Process(pid).as_dict(attrs=attrs_as_dict)
            list_process.append(dict_t)
        except:
            traceback.print_exc()
    return list_process


def get_updated_time(file_path_t):
    if os.path.isfile(file_path_t):
        return os.path.getmtime(file_path_t)
    else:
        return None


if __name__ == '__main__':
    # path_exe = r'E:\05_Resources\Softwares\PSASP\CriticalFiles_60000\WMLFRTMsg.exe'
    # path_env = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190422_MinInputs'
    path_exe = r'E:\05_Resources\Softwares\PSASP\CriticalFiles_60000\wmudrt.exe'
    path_env = r'E:\01_Research\98_Data\华中电网大数据\华中2016夏（故障卡汇总）\Temp'

    et = executor_PSASP_st(path_exe, path_env)
    et.execute_exe()
