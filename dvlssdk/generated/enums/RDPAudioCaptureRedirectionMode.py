from enum import Enum


class RDPAudioCaptureRedirectionMode(Enum):
    DoNotRecord = 0
    RecordFromThisComputer = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPAudioCaptureRedirectionMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPAudioCaptureRedirectionMode]
        return int_value in values
