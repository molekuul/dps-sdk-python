from enum import Enum


class CommandLineExecutionMode(Enum):
    Default = 0
    KeepOpen = 1
    Capture = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in CommandLineExecutionMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CommandLineExecutionMode]
        return int_value in values
