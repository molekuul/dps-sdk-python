from enum import Enum


class VNCAuthentificationType(Enum):
    Ard = 0
    ArdAskObserve = 1
    ArdAskControl = 2
    Invalid = 3
    MsLogon = 4
    none = 5
    Ultra = 6
    Vnc = 7

    @staticmethod
    def value_from_name(typename):
        for name, member in VNCAuthentificationType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in VNCAuthentificationType]
        return int_value in values
