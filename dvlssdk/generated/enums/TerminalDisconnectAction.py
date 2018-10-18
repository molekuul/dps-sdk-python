from enum import Enum


class TerminalDisconnectAction(Enum):
    Default = 0
    Close = 1
    KeepOpen = 2
    Reconnect = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalDisconnectAction.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalDisconnectAction]
        return int_value in values
