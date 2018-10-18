from enum import Enum


class RDPGatewayUsageMethod(Enum):
    ProxyModeNoneDirect = 0
    ModeDirect = 1
    ProxyModeDetect = 2
    ProxyModeDefault = 3
    NoneDetect = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPGatewayUsageMethod.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPGatewayUsageMethod]
        return int_value in values
