import re


class CalcIPV4:

    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

        self._set_broadcast()
        self._set_net()

    # getters
    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def prefix(self):
        return self._prefix

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def net(self):
        return self._net

    @property
    def ips_amount(self):
        return self._get_ips_amount()

    # setters
    @ip.setter
    def ip(self, value):
        if not self._ip_validator(value):
            raise ValueError('IP Inválido.')

        self._ip = value
        self._ip_binary = self._ip_to_binary(value)

    @mask.setter
    def mask(self, value):
        if not value:
            return

        if not self._ip_validator(value):
            raise ValueError('Máscara Inválida.')

        self._mask = value
        self._binary_mask = self._ip_to_binary(value)

        if not hasattr(self, 'prefix'):
            self.prefix = self._binary_mask.count('1')

    @prefix.setter
    def prefix(self, value):
        if not value:
            return

        if not isinstance(value, int):
            raise TypeError('O prefixo deve ser um número inteiro.')

        if value > 32:
            raise ValueError('O prefixo deve ter 32Bits.')

        self._prefix = value
        self._binary_mask = (value * '1').ljust(32, '0')

        if not hasattr(self, 'mask'):
            self.mask = self._binary_to_ip(self._binary_mask)

    # methods
    @staticmethod
    def _ip_validator(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_binary(ip):
        groups = ip.split('.')
        binary_groups = [bin(int(x))[2:].zfill(8) for x in groups]
        return ''.join(binary_groups)

    @staticmethod
    def _binary_to_ip(binary):
        n = 8

        groups = [str(int(binary[i:i+n], 2)) for i in range(0, 32, n)]

        return '.'.join(groups)

    def _set_broadcast(self):
        host_bits = 32 - self.prefix
        self._broadcast_binary = self._ip_binary[:self.prefix] + (
            host_bits * '1')

        self._broadcast = self._binary_to_ip(self._broadcast_binary)
        return self._broadcast

    def _set_net(self):
        host_bits = 32 - self.prefix
        self._net_binary = self._ip_binary[:self.prefix] + (host_bits * '0')

        self._net = self._binary_to_ip(self._net_binary)
        return self._net

    def _get_ips_amount(self):
        return 2 ** (32 - self.prefix)
