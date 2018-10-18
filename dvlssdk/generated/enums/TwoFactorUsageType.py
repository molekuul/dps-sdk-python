from enum import Enum


class TwoFactorUsageType(Enum):
    none = 0
    Optional = 1
    Required = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in TwoFactorUsageType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TwoFactorUsageType]
        return int_value in values
