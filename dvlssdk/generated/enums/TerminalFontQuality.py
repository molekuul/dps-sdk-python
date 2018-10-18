from enum import Enum


class TerminalFontQuality(Enum):
    Default = 0
    AntiAliased = 1
    NonAntiAliased = 2
    ClearType = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalFontQuality.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalFontQuality]
        return int_value in values
