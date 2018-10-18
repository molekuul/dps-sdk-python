from enum import Enum


class SaveMode(Enum):
    none = 0
    Add = 1
    Edit = 2
    Delete = 3
    View = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in SaveMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SaveMode]
        return int_value in values
