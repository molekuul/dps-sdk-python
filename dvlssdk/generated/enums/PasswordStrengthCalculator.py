from enum import Enum


class PasswordStrengthCalculator(Enum):
    Default = 0
    Legacy = 1
    Zxcvbn = 2
    KeePass = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in PasswordStrengthCalculator.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PasswordStrengthCalculator]
        return int_value in values
