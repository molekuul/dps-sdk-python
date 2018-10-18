from enum import Enum


class CheckOutMode(Enum):
    Default = 0
    NotSupported = 1
    Automatic = 2
    Manual = 3
    Inherited = 4
    Optional = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in CheckOutMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CheckOutMode]
        return int_value in values
