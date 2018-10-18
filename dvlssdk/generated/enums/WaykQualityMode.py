from enum import Enum


class WaykQualityMode(Enum):
    Default = 0
    Low = 1
    Medium = 2
    High = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in WaykQualityMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WaykQualityMode]
        return int_value in values
