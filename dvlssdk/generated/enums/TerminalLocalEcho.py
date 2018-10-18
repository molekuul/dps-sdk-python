from enum import Enum


class TerminalLocalEcho(Enum):
    Default = 0
    Auto = 1
    On = 2
    Off = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalLocalEcho.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalLocalEcho]
        return int_value in values
