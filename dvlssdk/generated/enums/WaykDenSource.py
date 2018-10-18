from enum import Enum


class WaykDenSource(Enum):
    Default = 0
    Cloud = 1
    Local = 2
    DataSource = 3
    Custom = 4
    Inherited = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in WaykDenSource.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WaykDenSource]
        return int_value in values
