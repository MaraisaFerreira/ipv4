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
            raise ValueError('IP Inválido.')

        self._ip = value

    @mask.setter
    def mask(self, value):

        if not value:
            return

        if not self._ip_validator(value):
            raise ValueError('Máscara Inválida.')

        self._mask = value
        self._binary_mask = self.ip_to_binary(self.mask)
        print(self._binary_mask)

    @prefix.setter
    def prefix(self, value):

        if not value:
            return

        if not isinstance(value, int):
            raise TypeError('O prefixo deve ser um número inteiro.')

        if value > 32:
            raise ValueError('O prefixo deve ter 32Bits.')

        self._prefix = value

    @staticmethod
    def _ip_validator(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def ip_to_binary(ip):
        groups = ip.split('.')
        binary_groups = [bin(int(x))[2:].zfill(8) for x in groups]
        return ''.join(binary_groups)
