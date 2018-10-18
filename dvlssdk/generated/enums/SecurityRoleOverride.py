from enum import Enum


class SecurityRoleOverride(Enum):
    Default = 0
    Custom = 1
    Inherited = 2
    Everyone = 3
    Never = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in SecurityRoleOverride.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SecurityRoleOverride]
        return int_value in values
