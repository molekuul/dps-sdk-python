from enum import Enum


class ForbiddenPasswordVerificationMode(Enum):
    Contains = 0
    Equals = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in ForbiddenPasswordVerificationMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ForbiddenPasswordVerificationMode]
        return int_value in values
