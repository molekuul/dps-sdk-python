from enum import Enum


class InternetProtocol(Enum):
    Default = 0
    IPv4 = 1
    IPv6 = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in InternetProtocol.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in InternetProtocol]
        return int_value in values
