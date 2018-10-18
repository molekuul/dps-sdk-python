from enum import Enum


class ScreenColor(Enum):
    C256 = 0
    C15Bits = 1
    C16Bits = 2
    C24Bits = 3
    C32Bits = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in ScreenColor.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ScreenColor]
        return int_value in values
