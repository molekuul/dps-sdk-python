from enum import Enum


class TerminalAutoWrap(Enum):
    Default = 0
    On = 1
    Off = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalAutoWrap.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalAutoWrap]
        return int_value in values
