import Gadgets_PSASP
import const
import math
import re


def parse_lines_PSASP(lines, dict_translate, pattern_parse=const.Pattern_read, multi_line=1, key_busno=None):
    if multi_line > 1:
        num_lines = len(lines)
        Ndiv = math.ceil(num_lines / multi_line)
        lines = [Gadgets_PSASP.cat_lists([lines[hh] for hh in range(h * multi_line, (h + 1) * multi_line)]) for h in
                 range(Ndiv)]

    list_dict_parsed = []
    append_no = isinstance(key_busno, str)
    for h in range(len(lines)):
        line_t = lines[h]
        if isinstance(line_t, str):
            if h==0 and str.find(line_t,'Created on')!=-1:
                continue
            contents = re.findall(pattern_parse, line_t)
            if contents:
                dict_t = [dict_translate[hh](contents[hh]) if dict_translate[hh]
                          else contents[hh] for hh in range(min([len(contents),len(dict_translate)]))]
                if append_no:
                    dict_t[key_busno] = h
                list_dict_parsed.append(dict_t)

    return list_dict_parsed
