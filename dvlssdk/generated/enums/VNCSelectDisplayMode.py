from enum import Enum


class VNCSelectDisplayMode(Enum):
    Default = 0
    Primary = 1
    Custom = 2
    Prompt = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in VNCSelectDisplayMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in VNCSelectDisplayMode]
        return int_value in values
