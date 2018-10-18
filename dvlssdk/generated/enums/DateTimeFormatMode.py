from enum import Enum


class DateTimeFormatMode(Enum):
    Default = 0
    US = 1
    Custom = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in DateTimeFormatMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DateTimeFormatMode]
        return int_value in values
