from enum import Enum


class RDPScreenSizingMode(Enum):
    Default = 0
    AutoScale = 1
    FitToWindow = 2
    Server = 3
    none = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPScreenSizingMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPScreenSizingMode]
        return int_value in values
