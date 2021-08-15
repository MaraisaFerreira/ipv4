import re


class CalcIPV4:

    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

    #getters
    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def prefix(self):
        return self._prefix

    #setters
    @ip.setter
    def ip(self, value):
        if not self._ip_validator(value):
            raise ValueError('Ip Inválido.')

        self._ip = value

    @mask.setter
    def mask(self, value):
        self._mask = value

    @prefix.setter
    def prefix(self, value):
        self._prefix = value

    @staticmethod
    def _ip_validator(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True


