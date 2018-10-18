from enum import Enum


class UserLicenseType(Enum):
    Other = 0
    PasswordVaultManager = 1
    PasswordVaultManagerOnline = 2
    PasswordVaultManagerServer = 3
    RDMOCustomInstallerService = 4
    RDMOOnlineBackup = 5
    RemoteDesktopManager = 6
    RemoteDesktopManagerJump = 7
    RemoteDesktopManagerOnline = 8
    RemoteDesktopManagerOnlineBackup = 9
    RemoteDesktopManagerServer = 10
    PasswordVaultManagerFree = 11
    RemoteDesktopManagerFree = 12
    Wayk = 13

    @staticmethod
    def value_from_name(typename):
        for name, member in UserLicenseType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in UserLicenseType]
        return int_value in values
