from enum import Enum


class WaykAccessControl(Enum):
    Default = 0
    Viewing = 1
    Interaction = 2
    Clipboard = 3
    FileTransfer = 4
    RemoteExecution = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in WaykAccessControl.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WaykAccessControl]
        return int_value in values
