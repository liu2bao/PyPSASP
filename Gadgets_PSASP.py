from itertools import chain


def cat_lists(L):
    lst = list(chain(*L))
    return lst


def convert2float_s(str_t):
    try:
        dig_t = float(str_t)
    except:
        dig_t = float('nan')
    return str_t
