from enum import Enum


class TelnetFunctionKeysMode(Enum):
    CommonExtended = 0
    Common = 1
    Linux = 2
    XtermR6 = 3
    VT400 = 4
    VT100Plus = 5
    Sco = 6
    CommonAlternative = 7
    VT52 = 8
    LinuxAlternative = 9
    ScoAlternative = 10
    Wyse60 = 11
    HpUx = 12
    Pick = 13

    @staticmethod
    def value_from_name(typename):
        for name, member in TelnetFunctionKeysMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TelnetFunctionKeysMode]
        return int_value in values
