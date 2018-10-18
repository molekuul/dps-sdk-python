from enum import Enum


class HandbookTemplateType(Enum):
    Tutorial = 0
    Empty = 1
    Custom = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in HandbookTemplateType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in HandbookTemplateType]
        return int_value in values
