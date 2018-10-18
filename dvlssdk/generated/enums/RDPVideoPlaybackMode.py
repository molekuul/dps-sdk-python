from enum import Enum


class RDPVideoPlaybackMode(Enum):
    Disabled = 0
    Default = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPVideoPlaybackMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPVideoPlaybackMode]
        return int_value in values
