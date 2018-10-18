from enum import Enum


class ProtocolHandlerAction(Enum):
    Unknown = 0
    Open = 1
    Edit = 2
    View = 3
    Find = 4
    OpenWithMacro = 5
    ExportReport = 6
    Select = 7

    @staticmethod
    def value_from_name(typename):
        for name, member in ProtocolHandlerAction.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ProtocolHandlerAction]
        return int_value in values
