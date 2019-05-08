from PyPSASP.constants import const
import math

def get_c_voltage(v_amp, v_deg):
    v_rad = math.radians(v_deg)
    v_real = v_amp*math.cos(v_rad)
    v_image = v_amp*math.sin(v_rad)
    return v_real,v_image

def convert_bus_voltage_single(dict_bus):
    v_real,v_image = get_c_voltage(dict_bus[const.VoltageKey],dict_bus[const.AngleKey])
    dict_bus[const.VoltageRealKey] =v_real
    dict_bus[const.VoltageImageKey] =v_image
    return dict_bus


def expand_lf(lf):
    lf_e = {(k,tuple([lf[k][hh][no] for no in dict_map_type2no[k]]),a):lf[k][hh][a]
            for k in dict_map_type2no.keys() for hh in range(len(lf[k])) for a in dict_map_type2attr[k]}
    return lf_e


dict_map_type2no = {const.LABEL_BUS: (const.BusNoKey,),
                    const.LABEL_ACLINE: (const.INoKey, const.JNoKey, const.IDNoKey),
                    const.LABEL_TRANSFORMER: (const.INoKey, const.JNoKey, const.IDNoKey),
                    const.LABEL_DCLINE: (const.INoKey, const.JNoKey, const.IDNoKey),
                    const.LABEL_GENERATOR: (const.BusNoKey,),
                    const.LABEL_LOAD: (const.BusNoKey, const.LoadNoKey),
                    }

dict_map_type2attr = {
    const.LABEL_BUS: (const.VoltageRealKey,const.VoltageImageKey),
    const.LABEL_ACLINE: (const.PiKey, const.QiKey, const.PjKey, const.QjKey, const.ACLineQciKey, const.ACLineQcjKey),
    const.LABEL_TRANSFORMER: (const.PiKey, const.QiKey, const.PjKey, const.QjKey),
    const.LABEL_DCLINE: (const.PiKey, const.QiKey),
    const.LABEL_GENERATOR: (const.GenPgKey,const.GenQgKey),
    const.LABEL_LOAD: (const.LoadPlKey,const.LoadQlKey),
}


class PSASP_Converter(object):
    def __init__(self):
        pass

    def convert_get2list(self, dict_get):
        list_get = []
        for ele_type, list_ele in dict_get.items():
            if list_ele:
                for hh in range(len(list_ele)):
                    ele = list_ele[hh]
                    list_get_t = [{const.EleTypeKey: ele_type, const.EleIdKey: hh, const.EleAttrNameKey: k,
                                   const.EleAttrValueKey: v} for k, v in ele.items()]
                    list_get.extend(list_get_t)
        return list_get

    def convert_get2dict(self, list_get):
        eleTypes = set([x[const.EleTypeKey] for x in list_get])
        idmax = {k: max([x[const.EleIdKey] for x in list_get if x[const.EleTypeKey] == k]) for k in eleTypes}
        dict_get = {k: [dict()] * (v + 1) for k, v in idmax.items()}
        for get_t in list_get:
            dict_get[get_t[const.EleTypeKey]][get_t[const.EleIdKey]][get_t[const.EleAttrNameKey]] = get_t[
                const.EleAttrValueKey]
        return dict_get


class LoadFlow(object):
    @property
    def dict_lf(self):
        return self.__dict_lf

    @dict_lf.setter
    def dict_lf(self,value):
        self.__dict_lf = value

    @property
    def dict_lf_expanded(self):
        if not self.__dict_lf_expanded:
            self.expand_dict_lf()
        return self.__dict_lf_expanded


    def __init__(self,dict_lf,bus_voltage_c_appended=False):
        self.__dict_lf = dict_lf
        self.__dict_lf_expanded = None
        self.__bus_volatage_c_appended = bus_voltage_c_appended

    def append_bus_voltage_c(self):
        data_buses = self.__dict_lf[const.LABEL_BUS]
        data_buses_a = [convert_bus_voltage_single(x) for x in data_buses]
        self.__dict_lf[const.LABEL_BUS] = data_buses_a

    def expand_dict_lf(self):
        if not self.__bus_volatage_c_appended:
            self.append_bus_voltage_c()
        self.__dict_lf_expanded = expand_lf(self.__dict_lf)
        return self.dict_lf_expanded



if __name__=='__main__':
    from PyPSASP.PSASPClasses.Parsers import PSASP_Parser
    from PyPSASP.utils import utils_gadgets
    # path_t = r'E:\01_Research\98_Data\华中电网大数据\华中2016夏（故障卡汇总）\Temp'
    # b = parse_all_results_lf(path_t, const.LABEL_BUS)
    path_t = r'E:\01_Research\98_Data\SmallSystem_PSASP\Temp_20190422_MinInputs'
    # path_t = r'E:\05_Resources\Softwares\PSASP\SST\sst_pre'
    Parser_t = PSASP_Parser(path_t)
    Converter_t = PSASP_Converter()
    lfr = Parser_t.parse_all_results_lf()
    list_lfr = Converter_t.convert_get2list(lfr)
    heads, values = utils_gadgets.formulate_list_of_dicts(list_lfr)
    from PyPSASP.utils.utils_sqlite import insert_from_list_to_db, read_db

    insert_from_list_to_db('temp.db', 'temp', heads, values)
    list_lfr = read_db('temp.db', 'temp', return_dict_form=True)
    dict_lfr = Converter_t.convert_get2dict(list_lfr)