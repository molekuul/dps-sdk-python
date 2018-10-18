from enum import Enum


class WaykAuthType(Enum):
    Default = 0
    PromptForPermission = 1
    SecureRemotePassword = 2
    Ntlm = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in WaykAuthType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WaykAuthType]
        return int_value in values
