from enum import Enum


class DisplayMonitor(Enum):
    Primary = 0
    Secondary = 1
    Current = 2
    Configured = 3
    Default = 4
    First = 5
    Second = 6
    Third = 7
    Fourth = 8
    Fifth = 9
    Sixth = 10

    @staticmethod
    def value_from_name(typename):
        for name, member in DisplayMonitor.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DisplayMonitor]
        return int_value in values
