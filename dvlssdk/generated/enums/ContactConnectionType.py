from enum import Enum


class ContactConnectionType(Enum):
    Default = 0
    Employee = 1
    Customer = 2
    Company = 3
    Supplier = 4
    Familly = 5
    Support = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in ContactConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ContactConnectionType]
        return int_value in values
