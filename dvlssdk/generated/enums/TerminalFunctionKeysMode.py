from enum import Enum


class TerminalFunctionKeysMode(Enum):
    Default = 0
    EscN = 1
    Linux = 2
    XtermR6 = 3
    VT400 = 4
    VT100Plus = 5
    SCO = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalFunctionKeysMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalFunctionKeysMode]
        return int_value in values
