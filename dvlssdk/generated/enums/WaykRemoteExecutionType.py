from enum import Enum


class WaykRemoteExecutionType(Enum):
    Run = 0
    Command = 1
    Process = 2
    ShellScript = 3
    BatchScript = 4
    PowerShell = 5
    AppleScript = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in WaykRemoteExecutionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WaykRemoteExecutionType]
        return int_value in values
