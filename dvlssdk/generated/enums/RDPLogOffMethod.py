from enum import Enum


class RDPLogOffMethod(Enum):
    Default = 0
    Automatic = 1
    RDMAgent = 2
    WMI = 3
    Macro = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPLogOffMethod.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPLogOffMethod]
        return int_value in values
