import os






class PSASP(object):
    @property
    def path_temp(self):
        return self._path_temp

    @path_temp.setter
    def path_temp(self, value):
        if not isinstance(value, str):
            raise ValueError('path_temp must be a string!')
        self._path_temp = value


    def __init__(self,path_temp):
        self.path_temp = path_temp