from enum import Enum


class ProxyTunnelType(Enum):
    Http = 0
    Socks4 = 1
    Socks4A = 2
    Socks5 = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in ProxyTunnelType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ProxyTunnelType]
        return int_value in values
