from enum import Enum


class BrowserExtensionLinkerCompareType(Enum):
    Default = 0
    RegexDomain = 1
    RegexURL = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in BrowserExtensionLinkerCompareType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in BrowserExtensionLinkerCompareType]
        return int_value in values
