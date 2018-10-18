from enum import Enum


class OfflineMode(Enum):
    Disabled = 0
    Cache = 1
    ReadOnly = 3
    ReadWrite = 7

    @staticmethod
    def value_from_name(typename):
        for name, member in OfflineMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in OfflineMode]
        return int_value in values
