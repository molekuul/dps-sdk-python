from enum import Enum


class ARDSessionSelectRequestType(Enum):
    AskToShare = 0
    Share = 1
    Virtual = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in ARDSessionSelectRequestType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ARDSessionSelectRequestType]
        return int_value in values
