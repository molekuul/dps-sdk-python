from enum import Enum


class ResetTwoFactorResult(Enum):
    AlreadyReset = 0
    Reset = 1
    InvalidUserOrPassword = 2
    LockedUser = 3
    NotApprovedUser = 4
    InvalidIP = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in ResetTwoFactorResult.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ResetTwoFactorResult]
        return int_value in values
