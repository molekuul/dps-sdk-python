from enum import Enum


class PrivateKeyType(Enum):
    NoKey = 0
    File = 1
    Data = 2
    Link = 3
    MyDefault = 4
    PrivateVault = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in PrivateKeyType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PrivateKeyType]
        return int_value in values
