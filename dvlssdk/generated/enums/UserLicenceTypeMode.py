from enum import Enum


class UserLicenceTypeMode(Enum):
    Default = 0
    ConnectionManagement = 1
    PasswordManagement = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in UserLicenceTypeMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in UserLicenceTypeMode]
        return int_value in values
