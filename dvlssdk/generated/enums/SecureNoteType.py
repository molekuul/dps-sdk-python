from enum import Enum


class SecureNoteType(Enum):
    Rtf = 0
    Text = 1
    Markdown = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in SecureNoteType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SecureNoteType]
        return int_value in values
