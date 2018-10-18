from enum import Enum


class ConnectionDisplayMode(Enum):
    External = 0
    Embedded = 1
    Default = 2
    Unknown = 3
    Undocked = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in ConnectionDisplayMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ConnectionDisplayMode]
        return int_value in values
