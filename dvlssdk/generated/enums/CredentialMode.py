from enum import Enum


class CredentialMode(Enum):
    Default = 0
    none = 1
    SameAsManagement = 2
    SessionCredentials = 3
    PromptForCredentials = 4
    CustomCredentials = 5
    CredentialRepository = 6
    MyPersonalCredentials = 7

    @staticmethod
    def value_from_name(typename):
        for name, member in CredentialMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CredentialMode]
        return int_value in values
