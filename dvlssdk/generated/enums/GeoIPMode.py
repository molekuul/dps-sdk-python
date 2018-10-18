from enum import Enum


class GeoIPMode(Enum):
    none = 0
    FreeGeoIP = 1
    MaxMind = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in GeoIPMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in GeoIPMode]
        return int_value in values
