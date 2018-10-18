from enum import Enum


class WifiSecurity(Enum):
    none = 0
    WEP = 1
    WPA = 2
    WPA2Personal = 3
    WPA2Enterprise = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in WifiSecurity.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WifiSecurity]
        return int_value in values
