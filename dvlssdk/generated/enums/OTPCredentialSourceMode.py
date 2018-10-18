from enum import Enum


class OTPCredentialSourceMode(Enum):
    Default = 0
    CredentialRepository = 1
    PrivateVault = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in OTPCredentialSourceMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in OTPCredentialSourceMode]
        return int_value in values
