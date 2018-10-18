from enum import Enum


class IntelligentCacheAction(Enum):
    AddUpdate = 0
    Delete = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in IntelligentCacheAction.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in IntelligentCacheAction]
        return int_value in values
