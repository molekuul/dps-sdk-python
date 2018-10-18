from enum import Enum


class VNCCursorMode(Enum):
    TrackLocally = 0
    RemoteDeal = 1
    DontShowRemote = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in VNCCursorMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in VNCCursorMode]
        return int_value in values
