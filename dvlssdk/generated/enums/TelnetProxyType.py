from enum import Enum


class TelnetProxyType(Enum):
    none = 0
    Socks4 = 1
    Socks4a = 2
    Socks5 = 3
    HttpConnect = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in TelnetProxyType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TelnetProxyType]
        return int_value in values
