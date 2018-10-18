from enum import Enum


class FtpProxyType(Enum):
    Socks4 = 0
    Socks4a = 1
    Socks5 = 2
    HttpConnect = 3
    FtpSite = 4
    FtpUser = 5
    FtpOpen = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in FtpProxyType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in FtpProxyType]
        return int_value in values
