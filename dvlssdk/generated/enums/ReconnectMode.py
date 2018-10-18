from enum import Enum


class ReconnectMode(Enum):
    Default = 0
    Full = 1
    SmartReconnect = 2
    Legacy = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in ReconnectMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ReconnectMode]
        return int_value in values
