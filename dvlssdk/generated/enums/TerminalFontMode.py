from enum import Enum


class TerminalFontMode(Enum):
    Default = 0
    Override = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalFontMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalFontMode]
        return int_value in values
