from enum import Enum


class ConnectionStatusBehavior(Enum):
    Default = 0
    Locked = 1
    Disabled = 2
    Warning = 3
    Expired = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in ConnectionStatusBehavior.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ConnectionStatusBehavior]
        return int_value in values
