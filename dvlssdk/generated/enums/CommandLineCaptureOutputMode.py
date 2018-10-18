from enum import Enum


class CommandLineCaptureOutputMode(Enum):
    Default = 0
    File = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in CommandLineCaptureOutputMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CommandLineCaptureOutputMode]
        return int_value in values
