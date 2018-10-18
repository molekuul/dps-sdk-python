from enum import Enum


class VNCType(Enum):
    RealVNC = 0
    TightVNC = 1
    UltraVNC = 2
    Configured = 3
    DefaultEmbeddedConfiguration = 4
    RealVNCPlus = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in VNCType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in VNCType]
        return int_value in values
