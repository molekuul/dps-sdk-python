from enum import Enum


class VascoPasswordFormat(Enum):
    OTP = 0
    Static = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in VascoPasswordFormat.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in VascoPasswordFormat]
        return int_value in values
