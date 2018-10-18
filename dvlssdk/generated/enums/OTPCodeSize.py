from enum import Enum


class OTPCodeSize(Enum):
    Six = 0
    Eight = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in OTPCodeSize.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in OTPCodeSize]
        return int_value in values
