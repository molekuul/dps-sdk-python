from enum import Enum


class RDPNetworkConnectionType(Enum):
    Default = 0
    Modem = 1
    LowSpeedBroadband = 2
    Satellite = 3
    HighSpeedBroadband = 4
    WAN = 5
    LAN = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPNetworkConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPNetworkConnectionType]
        return int_value in values
