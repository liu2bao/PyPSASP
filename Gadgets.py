import traceback
from itertools import chain
import shutil, os, re

import psutil

JoinSep = '_'

def cat_lists(L):
    lst = list(chain(*L))
    return lst


def convert2float_s(str_t):
    try:
        dig_t = float(str_t)
    except:
        dig_t = float('nan')
    return dig_t


def copyfiles(path_src, path_dst, files):
    if not os.path.isdir(path_dst):
        os.makedirs(path_dst)

    for file in files:
        file_src = os.path.join(path_src, file)
        file_dst = os.path.join(path_dst, file)
        shutil.copy(file_src, file_dst)


def delete_files_pattern(path_t, pattern):
    if isinstance(path_t, str) and isinstance(pattern, str):
        if os.path.isdir(path_t):
            files = os.listdir(path_t)
            files_d = [x for x in files if re.match(pattern, x)]
            for fd in files_d:
                try:
                    pfd = os.path.join(path_t, fd)
                    os.remove(pfd)
                except:
                    print('error in deleting %s' % fd)


def get_all_process_legacy():
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


def get_all_process(name=None):
    attrs_as_dict = ['pid', 'name', 'username', 'exe', 'create_time']
    list_process = []
    for r in psutil.process_iter():
        try:
            if (name is None) or (isinstance(name, str) and r.name() == name):
                dict_t = r.as_dict(attrs=attrs_as_dict)
                list_process.append(dict_t)
        except:
            traceback.print_exc()
    return list_process


def get_all_process_tasklist(name=None):
    keys = ['name', 'exe', 'type', '']
    r = os.popen('tasklist')
    A = r.read()
    B = [x.split() for x in A.split('\n')]
    # TODO: how to split??
    pass


def generate_new_files_save_yield(path_save, prefix_save, postfix_save='', try_ori=False, flag_dir = False,
                                  return_path = False, join_underline=True):
    if try_ori:
        count = -1
    else:
        count = 0
    max_count = 100000
    if isinstance(prefix_save, str) and isinstance(postfix_save, str):
        if join_underline and prefix_save[-1]!=JoinSep:
            prefix_save = prefix_save+JoinSep
        while count <= max_count:
            if count == -1:
                file_name = prefix_save.rstrip(JoinSep) + postfix_save
            else:
                file_name = prefix_save + str(count) + postfix_save
            file_path_t = os.path.join(path_save, file_name)
            if flag_dir:
                flag_t = os.path.isdir(file_path_t)
            else:
                flag_t = os.path.isfile(file_path_t)
            if not flag_t:
                if return_path:
                    rt = os.path.join(path_save,file_name)
                else:
                    rt = file_name
                yield rt
            count += 1