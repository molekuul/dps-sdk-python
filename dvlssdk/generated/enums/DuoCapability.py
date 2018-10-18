from enum import Enum


class DuoCapability(Enum):
    none = 0
    Push = 1
    Phone = 2
    Sms = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in DuoCapability.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DuoCapability]
        return int_value in values
