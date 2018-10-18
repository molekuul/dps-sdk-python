from enum import Enum


class LogMessageType(Enum):
    Default = 0
    Info = 1
    Warning = 2
    Debug = 3
    Error = 4
    ErrorSilent = 5
    Validation = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in LogMessageType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in LogMessageType]
        return int_value in values
