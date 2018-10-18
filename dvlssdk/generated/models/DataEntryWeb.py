from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *


class DataEntryWeb:
    def __init__(self):
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.EquivalentUrls = []
        self.PasswordItem = SensitiveItem()
        self.PrivateVaultSearchString = ''
        self.Url = ''
        self.WebDomain = ''
        self.WebUserName = ''

