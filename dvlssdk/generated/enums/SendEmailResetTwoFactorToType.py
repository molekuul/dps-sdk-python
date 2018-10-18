from enum import Enum


class SendEmailResetTwoFactorToType(Enum):
    Administrators = 0
    SpecificEmail = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in SendEmailResetTwoFactorToType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SendEmailResetTwoFactorToType]
        return int_value in values
