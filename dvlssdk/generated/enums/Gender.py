from enum import Enum


class Gender(Enum):
    Unspecified = 0
    Male = 1
    Female = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in Gender.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in Gender]
        return int_value in values
