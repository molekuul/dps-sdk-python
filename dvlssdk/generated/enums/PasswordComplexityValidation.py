from enum import Enum


class PasswordComplexityValidation(Enum):
    none = 0
    Default = 1
    Warn = 2
    Required = 3
    Inherited = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in PasswordComplexityValidation.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PasswordComplexityValidation]
        return int_value in values
