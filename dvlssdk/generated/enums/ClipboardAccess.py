from enum import Enum


class ClipboardAccess(Enum):
    none = 0
    Admin = 1
    Editor = 2
    All = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in ClipboardAccess.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ClipboardAccess]
        return int_value in values
