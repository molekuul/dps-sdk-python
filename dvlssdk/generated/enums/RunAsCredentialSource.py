from enum import Enum


class RunAsCredentialSource(Enum):
    none = 0
    CurrentSession = 1
    Custom = 2
    CredentialRepository = 3
    MyDefault = 4
    SameAsManagement = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in RunAsCredentialSource.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RunAsCredentialSource]
        return int_value in values
