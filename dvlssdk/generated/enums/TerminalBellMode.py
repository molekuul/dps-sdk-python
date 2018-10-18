from enum import Enum


class TerminalBellMode(Enum):
    Default = 0
    none = 1
    Sound = 2
    Visual = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalBellMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalBellMode]
        return int_value in values
