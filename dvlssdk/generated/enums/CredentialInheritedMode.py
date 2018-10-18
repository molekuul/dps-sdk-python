from enum import Enum


class CredentialInheritedMode(Enum):
    Default = 0
    Parent = 1
    Folder = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in CredentialInheritedMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CredentialInheritedMode]
        return int_value in values
