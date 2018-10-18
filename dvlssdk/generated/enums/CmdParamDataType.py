from enum import Enum


class CmdParamDataType(Enum):
    Unused = 0
    Text = 1
    Secured = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in CmdParamDataType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CmdParamDataType]
        return int_value in values
