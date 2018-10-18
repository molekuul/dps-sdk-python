from enum import Enum


class ApplicationPlatform(Enum):
    Default = 0
    Windows = 1
    Web = 2
    Mac = 3
    Android = 4
    IOS = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in ApplicationPlatform.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ApplicationPlatform]
        return int_value in values
