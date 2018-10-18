from enum import Enum


class AllowOffline(Enum):
    Default = 0
    true = 1
    false = 2
    Inherited = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in AllowOffline.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in AllowOffline]
        return int_value in values
