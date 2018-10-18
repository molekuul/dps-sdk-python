from enum import Enum


class SoundHook(Enum):
    BringToThisComputer = 0
    DoNotPlay = 1
    LeaveAtRemoteComputer = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in SoundHook.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SoundHook]
        return int_value in values
