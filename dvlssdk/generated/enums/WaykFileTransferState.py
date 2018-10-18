from enum import Enum


class WaykFileTransferState(Enum):
    Completed = 0
    Active = 1
    Canceled = 2
    Paused = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in WaykFileTransferState.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WaykFileTransferState]
        return int_value in values
