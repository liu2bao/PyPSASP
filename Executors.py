import psutil
import os


class executor_PSASP(object):
    def __init__(self,path_exe, path_env=None, path_flagfile=None):
        path_t, flag_t = os.path.split(path_flagfile)
        if not path_t:
            path_flagfile = os.path.join(path_env, path_flagfile)
        if not os.path.isfile(path_exe):
            path_t, exe_t = os.path.split(path_exe)
            path_exe = os.path.join(path_env,exe_t)
            if not os.path.isfile(path_exe):
                raise ValueError('%s not exist' % path_exe)
        self.__path_exe = path_exe
        self.__path_env = path_env
        self.__path_flagfile = path_flagfile


