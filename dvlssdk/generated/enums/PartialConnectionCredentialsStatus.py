from enum import Enum


class PartialConnectionCredentialsStatus(Enum):
    Default = 0
    NotFound = 1
    Prompt = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in PartialConnectionCredentialsStatus.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PartialConnectionCredentialsStatus]
        return int_value in values
