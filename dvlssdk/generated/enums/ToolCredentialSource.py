from enum import Enum


class ToolCredentialSource(Enum):
    none = 0
    CurrentSession = 1
    Custom = 2
    CredentialRepository = 3
    MyDefault = 4
    SameAsManagement = 5
    Personal = 6
    Inherited = 7
    Prompt = 8
    SpecifyAtExecution = 9

    @staticmethod
    def value_from_name(typename):
        for name, member in ToolCredentialSource.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ToolCredentialSource]
        return int_value in values
