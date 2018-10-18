from enum import Enum


class DuplicateAction(Enum):
    Cancel = 0
    Ignore = 1
    IgnoreAll = 2
    Overwrite = 3
    OverwriteAll = 4
    Add = 5
    AddAll = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in DuplicateAction.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DuplicateAction]
        return int_value in values
