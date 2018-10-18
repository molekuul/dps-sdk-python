from enum import Enum


class JumpType(Enum):
    Default = 0
    ParentConnection = 1
    Inherited = 2
    LinkedConnection = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in JumpType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in JumpType]
        return int_value in values
