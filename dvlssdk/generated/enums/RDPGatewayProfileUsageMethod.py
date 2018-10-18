from enum import Enum


class RDPGatewayProfileUsageMethod(Enum):
    Default = 0
    Explicit = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPGatewayProfileUsageMethod.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPGatewayProfileUsageMethod]
        return int_value in values
