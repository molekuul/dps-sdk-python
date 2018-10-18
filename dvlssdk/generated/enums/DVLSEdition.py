from enum import Enum


class DVLSEdition(Enum):
    none = 0
    SmallBusiness = 1
    Corporate = 2
    Platinum = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in DVLSEdition.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DVLSEdition]
        return int_value in values
