from enum import Enum


class AddEntryMode(Enum):
    Default = 0
    TemplateListWithBlank = 1
    TemplateListOnly = 2
    NoTemplate = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in AddEntryMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in AddEntryMode]
        return int_value in values
