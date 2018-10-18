from enum import Enum


class TwoFactorAuthenticationType(Enum):
    none = 0
    GoogleAuthenticator = 1
    Yubikey = 2
    Email = 3
    Sms = 4
    Duo = 5
    SafeNet = 6
    AuthAnvil = 7
    AzureMFA = 8
    Radius = 9
    VascoSoap = 10

    @staticmethod
    def value_from_name(typename):
        for name, member in TwoFactorAuthenticationType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TwoFactorAuthenticationType]
        return int_value in values
