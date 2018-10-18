from enum import Enum


class TeamViewerConnectionType(Enum):
    RemoteControl = 0
    Presentation = 1
    FileTranfer = 2
    VPN = 3
    Choose = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in TeamViewerConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TeamViewerConnectionType]
        return int_value in values
