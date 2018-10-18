from enum import Enum


class RDPVersion(Enum):
    Unknown = 0
    RDP50 = 1
    RDP60 = 2
    RDP61 = 3
    RDP70 = 4
    RDP80 = 5
    RDP81 = 6
    Default = 7
    FreeRDP = 8
    FreeRDP7 = 9

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPVersion.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPVersion]
        return int_value in values
