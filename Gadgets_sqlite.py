import os
import sqlite3
import const
import traceback
import datetime
import time
import Gadgets
import contextlib
from threading import Lock

DictLocks = {}

@contextlib.contextmanager
def my_sqlite3(db_path):
    global DictLocks
    if db_path not in DictLocks.keys():
        DictLocks[db_path] = Lock()
    if DictLocks[db_path].acquire():
        conn_temp = sqlite3.connect(db_path)
        cursor_temp = conn_temp.cursor()
        try:
            yield cursor_temp
        finally:
            conn_temp.commit()
            cursor_temp.close()
            conn_temp.close()
            DictLocks[db_path].release()




def execute_sql(db_path, X):
    with my_sqlite3(db_path) as cursor_temp:
        data = None
        try:
            cursor_temp.execute(X)
            data = cursor_temp.fetchall()
        except:
            traceback.print_exc()
        return data


def get_keys(db_path, table_name, return_type = False):
    with my_sqlite3(db_path) as cursor_temp:
        cursor_temp.execute("PRAGMA table_info(""%s"")" % table_name)
        keys_info = cursor_temp.fetchall()
    keys = [x[1] for x in keys_info]
    key_types = [x[2] for x in keys_info]
    if return_type:
        return keys,key_types
    else:
        return keys



def read_db(db_path, table_name, list_keys=None, str_where=r'', return_dict_form = False):
    keys_sel = []
    data = []
    if os.path.isfile(db_path):
        flag_not_list = False
        if isinstance(list_keys, str):
            list_keys = [list_keys]
            flag_not_list = True
        try:
            keys,types = get_keys(db_path,table_name,return_type=True)
            dict_key_types = {keys[h]:types[h] for h in range(len(keys))}
            if list_keys is None:
                dict_key_types_sel = dict_key_types.copy()
            else:
                dict_key_types_sel = {k:v for k,v in dict_key_types.items() if k in list_keys}
            if dict_key_types_sel:
                keys_sel = list(dict_key_types_sel.keys())
                key_f_t = ','.join([r'%s as "%s [%s]"' % (k,k,dict_key_types[k]) for k in keys_sel])
                X = r'SELECT %s FROM %s' % (key_f_t, table_name)
                #X = X.replace('[DATETIME]','[TIMESTAMP]')
                sqlite3.register_converter('DATETIME',lambda x:datetime.datetime.strptime(x.decode(),'%Y-%m-%d %H:%M:%S'))
                X = X + ' ' + str_where
                with my_sqlite3(db_path) as cursor_temp:
                    cursor_temp.execute(X)
                    data = cursor_temp.fetchall()
                if flag_not_list and data:
                    data = [x[0] for x in data]
        except:
            traceback.print_exc()
            print('error while reading %s.%s' % (db_path, table_name))

    if return_dict_form:
        if data:
            data_dict_form = [{keys_sel[h]: d[h] for h in range(len(keys_sel))} for d in data]
        else:
            data_dict_form = []
        return data_dict_form
    else:
        return keys_sel, data


def get_table_names(db_path):
    with my_sqlite3(db_path) as cursor_temp:
        cursor_temp.execute(r'SELECT name FROM sqlite_master;')
        d = cursor_temp.fetchall()
    table_names = [x[0] for x in d]
    return table_names


def create_table(db_path, table_name, dict_keys_type, primary_key=None,
                 with_time_stamp=True, key_time_stamp=const.KeyInsertTimeStamp):
    sup_path_record_file = os.path.abspath(os.path.dirname(db_path))
    if not os.path.exists(sup_path_record_file):
        os.makedirs(sup_path_record_file)

    table_names = get_table_names(db_path)
    if table_name not in table_names:

        dict_X_keys = {k: "%s %s" % (k, v) for k, v in dict_keys_type.items()}
        if primary_key in dict_X_keys.keys():
            dict_X_keys[primary_key] = dict_X_keys[primary_key] + r' PRIMARY KEY NOT NULL'

        if with_time_stamp:
            X_time_stamp = '%s TimeStamp NOT NULL DEFAULT (datetime(\'now\',\'localtime\'))' % key_time_stamp
            dict_X_keys[key_time_stamp] = X_time_stamp

        X_main = "CREATE TABLE %s(%s);" % (table_name, ','.join(dict_X_keys.values()))
        with my_sqlite3(db_path) as cursor_temp:
            cursor_temp.execute(X_main)



def add_keys(db_path, table_name, dict_keys_type):
    table_names = get_table_names(db_path)
    if table_name in table_names:
        with my_sqlite3(db_path) as cursor_temp:
            cursor_temp.execute("PRAGMA table_info(""%s"")" % table_name)
            keys_info = cursor_temp.fetchall()
            keys_existed = [x[1] for x in keys_info]
            keys_new = list(set(dict_keys_type.keys()).difference(keys_existed))
            for key_new in keys_new:
                cursor_temp.execute("ALTER TABLE %s add %s %s" % (table_name, key_new, dict_keys_type[key_new]))



def delete_list(db_path, table_name, ref_key, list_value_ref):
    table_names = get_table_names(db_path)
    if table_name in table_names:
        value_ref_f_t = '?'
        list_list_value_ref = [[x] for x in list_value_ref]
        X = r'DELETE FROM {} WHERE {}={}'.format(table_name, ref_key, value_ref_f_t)
        with my_sqlite3(db_path) as cursor_temp:
            cursor_temp.executemany(X, list_list_value_ref)



def insert_from_list_to_db(db_path, table_name, list_keys, list_data, primary_key=None,
                           with_time_stamp=True, key_time_stamp=const.KeyInsertTimeStamp,
                           dict_keys_type_set=None):
    if list_keys and list_data:
        if not isinstance(dict_keys_type_set,dict):
            dict_keys_type_set = {}
        if isinstance(list_keys,str):
            list_keys = [list_keys]
            list_data = [[x] for x in list_data]
        dict_keys_type = {list_keys[h]: dict_keys_type_set[list_keys[h]] if list_keys[h] in dict_keys_type_set.keys() else get_type_str_list([x[h] for x in list_data]) for h in range(len(list_keys))}
        create_table(db_path, table_name, dict_keys_type, primary_key, with_time_stamp, key_time_stamp)
        add_keys(db_path, table_name, dict_keys_type)
        key_f_t = ('(' + ','.join(['"{}"'] * len(list_keys)) + ')').format(*list_keys)
        data_f_t = ('(' + ','.join(['?'] * len(list_keys)) + ')')
        X = r'INSERT OR IGNORE INTO "{}" {} VALUES{}'.format(table_name, key_f_t, data_f_t)
        with my_sqlite3(db_path) as cursor_temp:
            cursor_temp.executemany(X, list_data)




def update_list_to_db_multiref(db_path, table_name, list_keys_update, list_data_update, keys_ref, list_values_ref,
                               str_where=r'', dict_keys_type_set=None):
    try:
        if list_keys_update and list_data_update:
            table_names = get_table_names(db_path)
            if table_name in table_names:
                if not isinstance(dict_keys_type_set,dict):
                    dict_keys_type_set = {}
                if isinstance(keys_ref, str):
                    keys_ref_t = [keys_ref]
                    list_values_ref_t = [[x] for x in list_values_ref]
                else:
                    keys_ref_t = keys_ref
                    list_values_ref_t = list_values_ref

                if isinstance(list_keys_update, str):
                    list_keys_update_t = [list_keys_update]
                    list_data_update_t = [[x] for x in list_data_update]
                else:
                    list_keys_update_t = list_keys_update
                    list_data_update_t = list_data_update

                dict_keys_type = {list_keys_update_t[h]: dict_keys_type_set[list_keys_update_t[h]] if list_keys_update_t[h] in dict_keys_type_set.keys() else get_type_str_list([x[h] for x in list_data_update_t]) for h in range(len(list_keys_update_t))}

                add_keys(db_path, table_name, dict_keys_type)
                key_and_data_f_t = ','.join([x + '=?' for x in list_keys_update_t])
                key_and_data_ref_t = ' AND '.join([k + '=?' for k in keys_ref_t])
                str_where_t = str_where.strip().lstrip(r'WHERE').lstrip('where')
                X = r'UPDATE {} SET {} WHERE {}{}'.format(table_name, key_and_data_f_t, key_and_data_ref_t, str_where_t)
                # cursor_temp.executemany(X,list_result)
                list_data = list_data_update_t.copy()
                for i in range(len(list_data)):
                    list_data[i] = list(list_data[i])
                    list_data[i].extend(list_values_ref_t[i])

                with my_sqlite3(db_path) as cursor_temp:
                    cursor_temp.executemany(X, list_data)
    except:
        traceback.print_exc()

def get_type_str(obj):
    # type_str = 'CHAR'
    if isinstance(obj, str):
        type_str = 'CHAR'
    elif isinstance(obj, bool):
        type_str = 'INTEGER'
    elif isinstance(obj, int):
        type_str = 'INTEGER'
    elif isinstance(obj, float):
        type_str = 'DOUBLE'
    elif isinstance(obj, datetime.datetime):
        type_str = 'DATETIME'
    else:
        type_str = 'CHAR'
    return type_str


def get_type_str_list(list_t):
    for obj in list_t:
        if obj is not None:
            type_str_t = get_type_str(obj)
            return type_str_t
    return 'CHAR'


if __name__=='__main__':
    db = r'F:\Data\Housing\Lianjia\DataWarehouse_new\db\dealed.db'
    update_list_to_db_multiref(db,'temp',None,None,None,None)