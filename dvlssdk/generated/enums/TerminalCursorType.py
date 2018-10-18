from enum import Enum


class TerminalCursorType(Enum):
    Default = 0
    Block = 1
    Underline = 2
    VerticalLine = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in TerminalCursorType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TerminalCursorType]
        return int_value in values
