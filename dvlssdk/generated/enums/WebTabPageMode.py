from enum import Enum


class WebTabPageMode(Enum):
    Automatic = 0
    Always = 1
    Never = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in WebTabPageMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WebTabPageMode]
        return int_value in values
