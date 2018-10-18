from enum import Enum


class PortForwardMode(Enum):
    Local = 0
    Remote = 1
    Dynamic = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in PortForwardMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PortForwardMode]
        return int_value in values
