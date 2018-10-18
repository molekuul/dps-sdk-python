from dvlssdk.generated.enums.AlternateTwoFactorType import *
from dvlssdk.generated.enums.AzureMFAMode import *
from dvlssdk.generated.enums.DuoCapability import *
from dvlssdk.generated.enums.TwoFactorAuthenticationType import *


class TwoFactorInfo:
    def __init__(self):
        self.AccountName = ''
        self.AlternateBackupCodesSalt = ''
        self.AlternateTwoFactorType = AlternateTwoFactorType(0)
        self.AuthenticationType = TwoFactorAuthenticationType(0)
        self.CountryCode = ''
        self.DuoSelectedCapability = DuoCapability(0)
        self.DuoSelectedDeviceID = ''
        self.DuoTrustedDevicesToken = ''
        self.IsConfigured = False
        self.IsDuoTrustedDevices = False
        self.IsPreConfigured = False
        self.IsTwilio = False
        self.Key = ''
        self.MfaMode = AzureMFAMode(0)
        self.Phone = ''
        self.PhoneExt = ''
        self.SafeAlternateBackupCodes = []
        self.ValidationCode = ''

