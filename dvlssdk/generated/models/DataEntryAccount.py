from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *


class DataEntryAccount:
    def __init__(self):
        self.Credentials = PartialConnectionCredentials()
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Domain = ''
        self.PasswordItem = SensitiveItem()
        self.Url = ''
        self.UserName = ''
        self.EquivalentUrls = []

