from enum import Enum


class TerminalCursorKeyMode(Enum):
    Default = 0
    Normal = 1
    Application = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalCursorKeyMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalCursorKeyMode]
        return int_value in values
