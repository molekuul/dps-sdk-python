from enum import Enum


class PasswordGeneratorMode(Enum):
    Default = 0
    SpecifiedSettings = 1
    HumanReadable = 2
    Pattern = 3
    Pronounceable = 4
    Strong = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in PasswordGeneratorMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PasswordGeneratorMode]
        return int_value in values
