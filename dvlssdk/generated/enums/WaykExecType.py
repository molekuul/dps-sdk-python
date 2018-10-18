from enum import Enum


class WaykExecType(Enum):
    Run = 0
    Command = 1
    Process = 2
    BatchScript = 3
    PowerShell = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in WaykExecType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WaykExecType]
        return int_value in values
