from enum import Enum


class PasswordComplexityUsage(Enum):
    Default = 0
    none = 1
    Enabled = 2
    EnabledWarning = 3
    Inherited = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in PasswordComplexityUsage.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PasswordComplexityUsage]
        return int_value in values
