from PyPSASP.constants import const
import math
import numpy as np


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
    def __init__(self, dict_lf, bus_voltage_c_appended=False):
        self.__bus_volatage_c_appended = bus_voltage_c_appended
        self.__dict_lf = dict_lf
        self.__dict_lf_expanded = None

    @property
    def dict_lf(self):
        return self.__dict_lf

    @property
    def dict_lf_expanded(self):
        if not self.__dict_lf_expanded:
            self.expand_dict_lf()
        return self.__dict_lf_expanded

    @dict_lf.setter
    def dict_lf(self, value):
        self.__dict_lf = value

    def append_bus_voltage_c(self):
        data_buses = self.__dict_lf[const.LABEL_BUS]
        data_buses_a = [convert_bus_voltage_single(x) for x in data_buses]
        self.__dict_lf[const.LABEL_BUS] = data_buses_a

    def expand_dict_lf(self):
        if not self.__bus_volatage_c_appended:
            self.append_bus_voltage_c()
        self.__dict_lf_expanded = expand_lf(self.__dict_lf)
        return self.dict_lf_expanded


class GridGraph:
    def __init__(self, lfs=None, lfr=None):
        self._lfs = lfs
        self._lfr = lfr
        self._bus_names = None
        self._bus_names_r = None
        self._Y = None
        self._flow = None
        self._injections = None

    @property
    def lfs(self):
        return self._lfs

    @property
    def lfr(self):
        return self._lfr

    @lfs.setter
    def lfs(self, lfs):
        self._lfs = lfs

    @lfr.setter
    def lfr(self, lfr):
        self._lfr = lfr

    def get_bus_names(self, reget=False):
        if (self._bus_names is None) or (self._bus_names_r is None) or reget:
            buses = self._lfs[const.LABEL_BUS]
            buses_r_no = [b[const.BusNoKey] for b in self._lfr[const.LABEL_BUS]]
            self._bus_names = [b[const.BusNameKey] for b in buses]
            self._bus_names_r = [self._bus_names[hh] for hh in buses_r_no]
        return self._bus_names, self._bus_names_r

    def get_Y(self, reget=False):
        if (self._Y is None) or reget:
            buses = self._lfs[const.LABEL_BUS]
            NB = len(buses)
            Y = np.zeros([NB, NB], dtype=np.complex128)
            for al in self._lfs[const.LABEL_ACLINE]:
                mark = al[const.MarkKey]
                if mark != 0:
                    i_idx = al[const.INoKey] - 1
                    j_idx = al[const.JNoKey] - 1
                    xt = al[const.R1Key] + al[const.X1Key] * 1j
                    jhalfb = al[const.ACLineHalfB1Key] * 1j
                    if mark == 1:
                        yt = 1 / xt
                        Y[[i_idx, j_idx, i_idx, j_idx], [j_idx, i_idx, i_idx, j_idx]] += [-yt, -yt, yt + jhalfb,
                                                                                          yt + jhalfb]
                    else:
                        if mark == 2:
                            idx_t = j_idx
                        elif mark == 3:
                            idx_t = i_idx
                        else:
                            continue
                        yt = 1 / (xt + 1 / jhalfb)
                        Y[idx_t, idx_t] += yt + jhalfb
            for tr in self._lfs[const.LABEL_TRANSFORMER]:
                mark = tr[const.MarkKey]
                if mark != 0:
                    i_idx = abs(tr[const.INoKey]) - 1
                    j_idx = abs(tr[const.JNoKey]) - 1
                    xt = tr[const.R1Key] + tr[const.X1Key] * 1j
                    tkc = tr[const.TransTkKey] * np.exp(np.radians(tr[const.TransShiftAngKey]) * 1j)
                    zm = tr[const.TransRmKey] + tr[const.TransXmKey] * 1j
                    yt = 1 / xt
                    if zm == 0:
                        ym = zm
                    else:
                        ym = 1 / zm
                    sij = -1 / tkc
                    sji = np.conj(sij)
                    sjj = sij * sji
                    Y[[i_idx, j_idx, i_idx, j_idx], [i_idx, j_idx, j_idx, i_idx]] += np.array([1, sjj, sij, sji]) * yt
                    Y[i_idx, i_idx] += ym
            self._Y = Y
        return self._Y

    def get_flow(self, reget=False):
        if (self._flow is None) or reget:
            Y = self.get_Y(reget)
            bus_r = self._lfr[const.LABEL_BUS]
            bus_r_idx = np.array([b[const.BusNoKey] for b in bus_r]) - 1
            idx_valid = np.argwhere(bus_r_idx>=0).flatten()
            bus_r_idx_valid = bus_r_idx[idx_valid]
            bus_r_valid = [bus_r[i] for i in idx_valid]
            bus_r_v_amp = np.array([b[const.VoltageKey] for b in bus_r_valid])
            bus_r_v_ang = np.array([b[const.AngleKey] for b in bus_r_valid])
            bus_r_v = bus_r_v_amp * np.exp(np.radians(bus_r_v_ang) * 1j)
            Y_r = Y[bus_r_idx_valid, :][:, bus_r_idx_valid]
            in_currents_r = np.matmul(Y_r, bus_r_v)
            flow_r = bus_r_v * np.conj(in_currents_r)
            self._flow = np.zeros(len(self._lfs[const.LABEL_BUS]), dtype=np.complex128)
            self._flow[bus_r_idx_valid] = flow_r
        return self._flow

    def get_injections(self, reget=False):
        if (self._injections is None) or reget:
            self._injections = np.zeros(len(self._lfs[const.LABEL_BUS]), dtype=np.complex128)
            for g in self._lfr[const.LABEL_GENERATOR]:
                self._injections[g[const.BusNoKey]-1] += g[const.GenPgKey] + g[const.GenQgKey] * 1j
            for l in self._lfr[const.LABEL_LOAD]:
                self._injections[l[const.BusNoKey]-1] -= l[const.LoadPlKey] + l[const.LoadQlKey] * 1j
            if self._lfr[const.LABEL_DCLINE]:
                for dl in self._lfr[const.LABEL_DCLINE]:
                    i_idx = dl[const.INoKey] - 1
                    j_idx = dl[const.JNoKey] - 1
                    Sdi = (dl[const.DCLinePd1iKey] + dl[const.DCLinePd2iKey]) + \
                          1j * (dl[const.DCLineQd1iKey] + dl[const.DCLineQd2iKey] + dl[const.DCLineQcipKey])
                    Sdj = (dl[const.DCLinePd1jKey] + dl[const.DCLinePd2jKey]) + \
                          1j * (dl[const.DCLineQd1jKey] + dl[const.DCLineQd2jKey] + dl[const.DCLineQcjpKey])
                    self._injections[i_idx] += Sdi
                    self._injections[j_idx] += Sdj
        return self._injections
