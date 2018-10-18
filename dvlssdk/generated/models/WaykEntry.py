from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.KeyboardHook import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.WaykAuthType import *
from dvlssdk.generated.enums.WaykQualityMode import *


class WaykEntry:
    def __init__(self):
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Host = ''
        self.KeyboardHook = KeyboardHook(0)
        self.PasswordItem = SensitiveItem()
        self.Port = 4489
        self.PreferredAuthType = WaykAuthType(0)
        self.PrivateVaultSearchString = ''
        self.QualityMode = WaykQualityMode(0)
        self.Scaled = False

