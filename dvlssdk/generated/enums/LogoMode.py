from enum import Enum


class LogoMode(Enum):
    none = 0
    Url = 1
    File = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in LogoMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in LogoMode]
        return int_value in values
