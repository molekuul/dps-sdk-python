from enum import Enum


class Days(Enum):
    Default = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 4
    Thursday = 8
    Friday = 16
    Saturday = 32
    Sunday = 64

    @staticmethod
    def value_from_name(typename):
        for name, member in Days.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in Days]
        return int_value in values
