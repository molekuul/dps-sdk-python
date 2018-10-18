from enum import Enum


class ConnectionSettingOverrideMode(Enum):
    none = 0
    Local = 1
    User = 2
    Both = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in ConnectionSettingOverrideMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ConnectionSettingOverrideMode]
        return int_value in values
