from enum import Enum


class RDPApplicationExternal(Enum):
    Default = 0
    Thinstuff = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPApplicationExternal.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPApplicationExternal]
        return int_value in values
