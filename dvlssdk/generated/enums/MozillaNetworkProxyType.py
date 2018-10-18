from enum import Enum


class MozillaNetworkProxyType(Enum):
    NoProxy = 0
    ManualProxyConfiguration = 1
    ProxyAutoConfiguration = 2
    AutoDetectProxySettings = 4
    UseSystemProxySettings = 5
    Default = -1

    @staticmethod
    def value_from_name(typename):
        for name, member in MozillaNetworkProxyType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in MozillaNetworkProxyType]
        return int_value in values
