from enum import Enum


class GroupConnectionType(Enum):
    Folder = 0
    Site = 1
    Company = 2
    Workstation = 3
    Server = 4
    Device = 5
    Identity = 6
    Customer = 7
    Database = 8
    Printer = 9
    Domain = 10
    Software = 11

    @staticmethod
    def value_from_name(typename):
        for name, member in GroupConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in GroupConnectionType]
        return int_value in values
