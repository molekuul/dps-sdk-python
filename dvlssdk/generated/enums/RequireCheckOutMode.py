from enum import Enum


class RequireCheckOutMode(Enum):
    Default = 0
    true = 1
    false = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in RequireCheckOutMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RequireCheckOutMode]
        return int_value in values
