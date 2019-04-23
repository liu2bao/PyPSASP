import os
import sqlite3
import const
import traceback
import datetime
import time
import Gadgets


def execute_sql(db_path, X):
    conn_temp = sqlite3.connect(db_path)
    cursor_temp = conn_temp.cursor()
    data = None
    try:
        cursor_temp.execute(X)
        data = cursor_temp.fetchall()
    except:
        traceback.print_exc()
    conn_temp.commit()
    cursor_temp.close()
    conn_temp.close()
    return data


def get_keys(db_path, table_name, return_type = False):
    conn_temp = sqlite3.connect(db_path)
    cursor_temp = conn_temp.cursor()
    cursor_temp.execute("PRAGMA table_info(""%s"")" % table_name)
    keys_info = cursor_temp.fetchall()
    cursor_temp.close()
    conn_temp.close()
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
                conn_temp = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
                cursor_temp = conn_temp.cursor()
                X = X + ' ' + str_where
                cursor_temp.execute(X)
                data = cursor_temp.fetchall()
                cursor_temp.close()
                conn_temp.close()

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
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(r'SELECT name FROM sqlite_master;')
    d = cursor.fetchall()
    cursor.close()
    conn.close()
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

        conn_temp = sqlite3.connect(db_path)
        cursor_temp = conn_temp.cursor()
        cursor_temp.execute(X_main)
        conn_temp.commit()
        cursor_temp.close()
        conn_temp.close()


def add_keys(db_path, table_name, dict_keys_type):
    table_names = get_table_names(db_path)
    if table_name in table_names:
        conn_temp = sqlite3.connect(db_path)
        cursor_temp = conn_temp.cursor()
        cursor_temp.execute("PRAGMA table_info(""%s"")" % table_name)
        keys_info = cursor_temp.fetchall()
        keys_existed = [x[1] for x in keys_info]
        keys_new = list(set(dict_keys_type.keys()).difference(keys_existed))
        for key_new in keys_new:
            cursor_temp.execute("ALTER TABLE %s add %s %s" % (table_name, key_new, dict_keys_type[key_new]))
        conn_temp.commit()
        cursor_temp.close()
        conn_temp.close()


def delete_list(db_path, table_name, ref_key, list_value_ref):
    table_names = get_table_names(db_path)
    if table_name in table_names:
        conn_temp = sqlite3.connect(db_path)
        cursor_temp = conn_temp.cursor()
        value_ref_f_t = '?'
        list_list_value_ref = [[x] for x in list_value_ref]
        X = r'DELETE FROM {} WHERE {}={}'.format(table_name, ref_key, value_ref_f_t)
        cursor_temp.executemany(X, list_list_value_ref)
        conn_temp.commit()
        cursor_temp.close()
        conn_temp.close()


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
        conn_temp = sqlite3.connect(db_path)
        cursor_temp = conn_temp.cursor()
        key_f_t = ('(' + ','.join(['"{}"'] * len(list_keys)) + ')').format(*list_keys)
        data_f_t = ('(' + ','.join(['?'] * len(list_keys)) + ')')
        X = r'INSERT OR IGNORE INTO "{}" {} VALUES{}'.format(table_name, key_f_t, data_f_t)
        # cursor_temp.executemany(X,list_result)
        cursor_temp.executemany(X, list_data)
        conn_temp.commit()
        cursor_temp.close()
        conn_temp.close()



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

