from enum import Enum


class DataEntryWalletType(Enum):
    DriverLicense = 0
    SocialSecurityNumber = 1
    Membership = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in DataEntryWalletType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DataEntryWalletType]
        return int_value in values
