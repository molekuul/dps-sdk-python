from enum import Enum


class TerminalLogOverwriteMode(Enum):
    Default = 0
    Prompt = 1
    Append = 2
    Overwrite = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalLogOverwriteMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalLogOverwriteMode]
        return int_value in values
