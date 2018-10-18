from enum import Enum


class ServerUserType(Enum):
    Builtin = 0
    LocalWindows = 1
    SqlServer = 2
    Domain = 3
    Office365 = 4
    none = 5
    Cloud = 6
    Legacy = 7
    AzureAD = 8

    @staticmethod
    def value_from_name(typename):
        for name, member in ServerUserType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ServerUserType]
        return int_value in values
