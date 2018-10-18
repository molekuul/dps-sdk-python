from enum import Enum


class KeyboardHook(Enum):
    OnTheLocalComputer = 0
    OnTheRemoteComputer = 1
    InFullScreenMode = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in KeyboardHook.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in KeyboardHook]
        return int_value in values
