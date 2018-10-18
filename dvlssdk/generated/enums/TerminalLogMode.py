from enum import Enum


class TerminalLogMode(Enum):
    Event = 0
    AllPrintableOutput = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalLogMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalLogMode]
        return int_value in values
