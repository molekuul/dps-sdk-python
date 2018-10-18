from enum import Enum


class RDPClientSpec(Enum):
    Default = 0
    FullMode = 1
    ThinClientMode = 2
    SmallCacheMode = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPClientSpec.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPClientSpec]
        return int_value in values
