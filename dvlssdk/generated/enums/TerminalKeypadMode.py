from enum import Enum


class TerminalKeypadMode(Enum):
    Default = 0
    Enable = 1
    Disable = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalKeypadMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalKeypadMode]
        return int_value in values
