from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *


class RootDetail:
    def __init__(self):
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Domain = ''
        self.PasswordItem = SensitiveItem()
        self.UserName = ''

