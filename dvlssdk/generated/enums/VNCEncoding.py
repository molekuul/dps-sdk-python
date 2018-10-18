from enum import Enum


class VNCEncoding(Enum):
    Default = 0
    Auto = 1
    CoRRE = 2
    Hextile = 3
    Raw = 4
    RRE = 5
    Tight = 6
    Ultra = 7
    Zlib = 8
    ZlibHEX = 9
    ZlibHalftone = 10
    Zlib16Gray = 11
    ZlibThousands = 12
    Zrle = 13

    @staticmethod
    def value_from_name(typename):
        for name, member in VNCEncoding.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in VNCEncoding]
        return int_value in values
