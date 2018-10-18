from enum import Enum


class CustomInstallerStatus(Enum):
    Created = 0
    InProgress = 1
    Fail = 2
    Success = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in CustomInstallerStatus.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CustomInstallerStatus]
        return int_value in values
