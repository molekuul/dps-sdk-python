from enum import Enum


class ProxyMode(Enum):
    none = 0
    Link = 1
    Custom = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in ProxyMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ProxyMode]
        return int_value in values
