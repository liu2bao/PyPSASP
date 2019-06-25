from PyPSASP.constants import const
import math


def get_c_voltage(v_amp, v_deg):
    v_rad = math.radians(v_deg)
    v_real = v_amp * math.cos(v_rad)
    v_image = v_amp * math.sin(v_rad)
    return v_real, v_image


def convert_bus_voltage_single(dict_bus):
    v_real, v_image = get_c_voltage(dict_bus[const.VoltageKey], dict_bus[const.AngleKey])
    dict_bus[const.VoltageRealKey] = v_real
    dict_bus[const.VoltageImageKey] = v_image
    return dict_bus


def expand_lf(lf):
    lf_e = {(k, tuple([lf[k][hh][no] for no in dict_map_type2no[k]]), a): lf[k][hh][a]
            for k in dict_map_type2no.keys() for hh in range((len(lf[k]) if lf[k] else 0))
            for a in dict_map_type2attr[k]}
    return lf_e


dict_map_type2no = {const.LABEL_BUS: (const.BusNoKey,),
                    const.LABEL_ACLINE: (const.INoKey, const.JNoKey, const.IDNoKey),
                    const.LABEL_TRANSFORMER: (const.INoKey, const.JNoKey, const.IDNoKey),
                    const.LABEL_DCLINE: (const.INoKey, const.JNoKey, const.IDNoKey),
                    const.LABEL_GENERATOR: (const.BusNoKey,),
                    const.LABEL_LOAD: (const.BusNoKey, const.LoadNoKey),
                    }

dict_map_type2attr = {
    const.LABEL_BUS: (const.VoltageRealKey, const.VoltageImageKey),
    const.LABEL_ACLINE: (const.PiKey, const.QiKey, const.PjKey, const.QjKey, const.ACLineQciKey, const.ACLineQcjKey),
    const.LABEL_TRANSFORMER: (const.PiKey, const.QiKey, const.PjKey, const.QjKey),
    const.LABEL_DCLINE: (const.PiKey, const.QiKey),
    const.LABEL_GENERATOR: (const.GenPgKey, const.GenQgKey),
    const.LABEL_LOAD: (const.LoadPlKey, const.LoadQlKey),
}


class LoadFlow(object):
    @property
    def dict_lf(self):
        return self.__dict_lf

    @dict_lf.setter
    def dict_lf(self, value):
        self.__dict_lf = value

    @property
    def dict_lf_expanded(self):
        if not self.__dict_lf_expanded:
            self.expand_dict_lf()
        return self.__dict_lf_expanded

    def __init__(self, dict_lf, bus_voltage_c_appended=False):
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
