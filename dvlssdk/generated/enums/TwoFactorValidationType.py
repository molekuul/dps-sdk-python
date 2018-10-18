from enum import Enum


class TwoFactorValidationType(Enum):
    Success = 0
    Invalid = 1
    UserDeny = 2
    SecondStepIsRequired = 3
    ValidationCodeIsEmpty = 4
    SmsSended = 5
    Fraud = 6
    Timeout = 7
    Lockedout = 8

    @staticmethod
    def value_from_name(typename):
        for name, member in TwoFactorValidationType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TwoFactorValidationType]
        return int_value in values
