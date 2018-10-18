from enum import Enum


class ChromeProxyType(Enum):
    Default = 0
    none = 1
    Http = 2
    Https = 3
    Socks4 = 4
    Socks4a = 5
    Socks5 = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in ChromeProxyType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ChromeProxyType]
        return int_value in values
