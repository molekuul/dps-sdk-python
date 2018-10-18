from enum import Enum


class TerminalHomeEndKeyMode(Enum):
    Default = 0
    Standard = 1
    Rxvt = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalHomeEndKeyMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalHomeEndKeyMode]
        return int_value in values
