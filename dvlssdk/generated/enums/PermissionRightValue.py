from enum import Enum


class PermissionRightValue(Enum):
    Default = 0
    Denied = 1
    Allow = 2
    none = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in PermissionRightValue.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PermissionRightValue]
        return int_value in values
