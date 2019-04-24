import psutil
import os
from threading import Thread, Lock
import time
import traceback
import const
import Gadgets

# TempBat = 'temp.bat'
Lock_GetProcess = Lock()
Lock_WriteBat = Lock()


class executor_PSASP(object):
    def __init__(self, path_exe, path_env=None, path_flagfile=None, patterns_del=None, hide_window=None):
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
        self.__patterns_del = patterns_del
        self.__hide_window = hide_window

    def __update_process(self):
        self.__current_process = Gadgets.get_all_process()

    def __get_process_inc(self):
        process_new = Gadgets.get_all_process()
        pid_old = [x['pid'] for x in self.__current_process]
        process_inc = [x for x in process_new if x['pid'] not in pid_old]
        return process_inc

    def __get_process_inc_matched(self, wait_time=0.5, max_try=10):
        process_inc_matched = []
        count = 0
        flag_found = False
        while count <= max_try:
            process_inc = self.__get_process_inc()
            process_inc_matched = [x for x in process_inc if x['exe'] == self.__path_exe]
            if not process_inc_matched:
                time.sleep(wait_time)
            else:
                flag_found = True
                break
            count += 1
        if flag_found:
            pid = process_inc_matched[0]['pid']
            self.hide_window(pid)
        return process_inc_matched

    def __update_mtime_flagfile(self):
        self.__flagfile_last_update_time = get_updated_time(self.__path_flagfile)

    def __kill_process_while_flag(self, wait_time=2, max_try=60):
        count = 0
        while count <= max_try:
            if os.path.isfile(self.__path_flagfile):
                if self.__flagfile_last_update_time is None:
                    break
                elif get_updated_time(self.__path_flagfile) <= self.__flagfile_last_update_time:
                    break
            time.sleep(wait_time)
            count += 1
        if count >= max_try:
            print('maximum try reached')
        for process_t in self.__process_inc_matched:
            os.system(r'taskkill /pid %d -t -f' % process_t['pid'])
            # print('process killed')

    def delete_files_with_pattern(self):
        if self.__path_env:
            for pattern_t in self.__patterns_del:
                Gadgets.delete_files_pattern(self.__path_env, pattern_t)

    def execute_exe(self):
        temp_bat = None
        if self.__path_env:
            self.delete_files_with_pattern()
            idx_drive_t = str.find(self.__path_env, ':')
            if idx_drive_t == -1:
                raise ValueError('Drive not found')
            drive_t = self.__path_env[:idx_drive_t + 1]
            temp_bat = next(Gadgets.generate_new_files_save_yield('tempBats', 'temp', '.bat'))
            if not os.path.isdir('tempBats'):
                os.makedirs('tempBats')
            with open(temp_bat, 'w') as f:
                f.write('%s\n' % drive_t)
                f.write('cd "%s"\n' % self.__path_env)
                f.write('"%s"' % self.__path_exe)
            exe_t = temp_bat
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
            thread_kill.start()
            thread_kill.join()
            thread_exe.join()
        if temp_bat:
            try:
                os.remove(temp_bat)
            except:
                print('error while removing %s' % temp_bat)

    def hide_window(self, pid):
        if isinstance(self.__hide_window, str):
            pass
            # TODO: how to hide window more elegantly?
            #Gadgets.hide_window_by_name(self.__hide_window)


class executor_PSASP_lf(executor_PSASP):
    def __init__(self, path_exe, path_env):
        flag_file_lf = const.dict_mapping_files[const.LABEL_LF][const.LABEL_RESULTS][const.LABEL_CONF]
        executor_PSASP.__init__(self, path_exe, path_env, patterns_del=(flag_file_lf,))


class executor_PSASP_st(executor_PSASP):
    def __init__(self, path_exe, path_env):
        flag_file_st = const.dict_mapping_files[const.LABEL_ST][const.LABEL_RESULTS][const.LABEL_CONF]
        patterns_del = (const.PATTERN_OUTPUT_ST, flag_file_st)
        executor_PSASP.__init__(self, path_exe, path_env, flag_file_st, patterns_del,
                                hide_window=const.WINDOW_NAME_ST)

class executor_PSASP_sstlin(executor_PSASP):
    def __init__(self, path_exe, path_env):
        flag_file_sst_lin = const.dict_mapping_files[const.LABEL_SST_LIN][const.LABEL_RESULTS][const.LABEL_CONF]
        patterns_del = (flag_file_sst_lin,)
        executor_PSASP.__init__(self, path_exe, path_env, path_flagfile=None, patterns_del=patterns_del)


class executor_PSASP_ssteig(executor_PSASP):
    def __init__(self, path_exe, path_env):
        flag_file_sst_eig = const.dict_mapping_files[const.LABEL_SST_EIG][const.LABEL_RESULTS][const.LABEL_CONF]
        patterns_del = (flag_file_sst_eig,)
        executor_PSASP.__init__(self, path_exe, path_env, flag_file_sst_eig, patterns_del)


def get_updated_time(file_path_t):
    if os.path.isfile(file_path_t):
        return os.path.getmtime(file_path_t)
    else:
        return None


if __name__ == '__main__':
    # path_exe = r'E:\05_Resources\Softwares\PSASP\CriticalFiles_60000\WMLFRTMsg.exe'
    # path_env = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190422_MinInputs'
    # path_exe = r'E:\05_Resources\Softwares\PSASP\CriticalFiles_60000\wmudrt.exe'
    # path_exe = r'E:\05_Resources\Softwares\PSASP\CriticalFiles\Wsstlin.exe'
    path_exe_sstlin = r'E:\CNN\PSASP_SST\Temp2\Wsstlin.exe'
    path_exe_ssteig = r'E:\CNN\PSASP_SST\Temp2\Wssteig.exe'
    path_env = r'E:\CNN\PSASP_SST\Temp2'

    et1 = executor_PSASP_sstlin(path_exe_sstlin, path_env)
    et2 = executor_PSASP_ssteig(path_exe_ssteig, path_env)
    et1.execute_exe()
    et2.execute_exe()
