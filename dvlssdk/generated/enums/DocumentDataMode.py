from enum import Enum


class DocumentDataMode(Enum):
    Link = 0
    EmbeddedInConnection = 1
    EmbeddedInAttachment = 2
    Url = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in DocumentDataMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DocumentDataMode]
        return int_value in values
