from enum import Enum


class SIDTypes(Enum):
    none = 0
    User = 1
    Group = 2
    Domain = 3
    Alias = 4
    WellKnownGroup = 5
    DeletedAccount = 6
    Invalid = 7
    Unknown = 8
    Computer = 9

    @staticmethod
    def value_from_name(typename):
        for name, member in SIDTypes.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SIDTypes]
        return int_value in values
