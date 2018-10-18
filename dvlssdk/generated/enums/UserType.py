from enum import Enum


class UserType(Enum):
    Admin = 0
    User = 1
    Restricted = 2
    ReadOnly = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in UserType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in UserType]
        return int_value in values
