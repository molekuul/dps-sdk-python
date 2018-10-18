from enum import Enum


class SubscriptionProductType(Enum):
    none = 0
    Basic = 1
    Pro = 2
    Enterprise = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in SubscriptionProductType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SubscriptionProductType]
        return int_value in values
