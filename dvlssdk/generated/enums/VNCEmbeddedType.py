from enum import Enum


class VNCEmbeddedType(Enum):
    Default = 0
    UltraVNC = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in VNCEmbeddedType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in VNCEmbeddedType]
        return int_value in values
