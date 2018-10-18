from enum import Enum


class RDPType(Enum):
    Normal = 0
    Azure = 1
    HyperV = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPType]
        return int_value in values
