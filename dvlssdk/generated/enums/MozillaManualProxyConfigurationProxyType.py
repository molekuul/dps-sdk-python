from enum import Enum


class MozillaManualProxyConfigurationProxyType(Enum):
    Default = 0
    Http = 1
    Ftp = 2
    Socks = 3
    Ssl = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in MozillaManualProxyConfigurationProxyType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in MozillaManualProxyConfigurationProxyType]
        return int_value in values
