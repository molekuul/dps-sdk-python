from enum import Enum


class ConnectionLogGridDateKind(Enum):
    OriginalTime = 0
    UtcToLocalTime = 1
    Utc = 2
    Custom = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in ConnectionLogGridDateKind.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ConnectionLogGridDateKind]
        return int_value in values
