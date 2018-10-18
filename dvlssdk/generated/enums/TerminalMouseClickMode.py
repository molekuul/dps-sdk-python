from enum import Enum


class TerminalMouseClickMode(Enum):
    Default = 0
    Windows = 1
    Compromise = 2
    XTerm = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalMouseClickMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalMouseClickMode]
        return int_value in values
