from enum import Enum


class VNCColorDepth(Enum):
    CFull = 0
    C8Bit = 1
    C256 = 2
    C64 = 3
    C8 = 4
    C8Grey = 5
    C4Grey = 6
    C2Grey = 7

    @staticmethod
    def value_from_name(typename):
        for name, member in VNCColorDepth.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in VNCColorDepth]
        return int_value in values
