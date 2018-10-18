from enum import Enum


class InvalidIpFormat(Enum):
    AllowedSingle = 0
    AllowedMasked = 1
    DeniedSingle = 2
    DeniedMasked = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in InvalidIpFormat.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in InvalidIpFormat]
        return int_value in values
