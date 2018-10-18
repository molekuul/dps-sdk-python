from enum import Enum


class AlternateTwoFactorType(Enum):
    none = 0
    Email = 1
    BackupCodes = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in AlternateTwoFactorType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in AlternateTwoFactorType]
        return int_value in values
