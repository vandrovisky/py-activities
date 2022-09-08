import re

class CalcIPv4:
    def __init__(self, ip, mask=None, pref=None):
        self.ip = ip
        self.mask = mask
        self.pref = pref

        self._set_broadcast()
        self._set_network()

        print(self.ip)
        print(self.mask)
        print(self.pref)
        print(self._network)
        print(self._broadcast)
        print(self._get_num_ip())

    @property
    def ip(self):
        return self._ip
    @property
    def mask(self):
        return self._mask
    @property
    def pref(self):
        return self._pref

    @ip.setter
    def ip(self,ip):
        if not self._validate_ip(ip):
            raise ValueError('ip Invalido')
        self._ip = ip
        self._ip_bin = self._ip_to_bin(ip)

    @mask.setter
    def mask(self,mask):
        if not mask:
            return

        if not self._validate_ip(mask):
            raise ValueError('mascara invalida')

        self._mask = mask
        self._mask_bin = self._ip_to_bin(mask)
        
        if not hasattr(self, 'pref'):
            self.pref = self._mask_bin.count('1')

    @pref.setter
    def pref(self,pref):
        if not pref:
            return
        
        if not isinstance(pref, int):
            raise TypeError('Prefixo necessita ser um numero inteiro')

        if pref > 32:
            raise ('error argumento maior que 32bits')
        self._pref = pref
        self._mask_bin = (pref * '1').ljust(32,'0')
        if not hasattr(self, 'mask'):
            self.mask = self._bin_to_ip(self._mask_bin)

    @staticmethod
    def _validate_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        if regexp.search(ip):
           return True

    @staticmethod
    def _ip_to_bin(ip): 
        blocks = ip.split('.')
        bin_blocks = [bin(int(x))[2:].zfill(8) for x in blocks]
        return ''.join(bin_blocks)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocks = [str(int(ip[i:n+i], 2)) for i in range(0,32,n)]
        return '.'.join(blocks)

    def _set_broadcast(self):
        host_bits = 32-self.pref
        self._broadcast_bin = self._ip_bin[:self.pref] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast
    
    def _set_network(self):
        host_bits = 32-self.pref
        self._network_bin = self._ip_bin[:self.pref] + (host_bits * '0')
        self._network = self._bin_to_ip(self._network_bin)
        return self._network

    def _get_num_ip(self):
        self._num_ip = (2** (32-self.pref)) -2
        return self._num_ip