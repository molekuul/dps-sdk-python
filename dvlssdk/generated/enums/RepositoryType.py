from enum import Enum


class RepositoryType(Enum):
    DVLS = 0
    Asset = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in RepositoryType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RepositoryType]
        return int_value in values
