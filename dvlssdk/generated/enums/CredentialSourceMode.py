from enum import Enum


class CredentialSourceMode(Enum):
    SessionSpecific = 0
    CredentialEntry = 1
    Embedded = 2
    Parent = 3
    Inherited = 4
    MyDefault = 5
    Personal = 6
    none = 7
    Prompt = 8
    CurrentSession = 9
    SameAsManagement = 10
    PrivateVaultSearch = 11
    SpecifyAtExecution = 12

    @staticmethod
    def value_from_name(typename):
        for name, member in CredentialSourceMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CredentialSourceMode]
        return int_value in values
