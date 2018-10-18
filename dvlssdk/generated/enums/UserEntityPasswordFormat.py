from enum import Enum


class UserEntityPasswordFormat(Enum):
    Legacy = 0
    IdentityV2 = 1
    IdentityV3 = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in UserEntityPasswordFormat.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in UserEntityPasswordFormat]
        return int_value in values
