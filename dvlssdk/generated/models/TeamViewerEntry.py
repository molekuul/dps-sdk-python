from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.TeamViewerConnectionType import *


class TeamViewerEntry:
    def __init__(self):
        self.ConnectionType = TeamViewerConnectionType(0)
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Id = ''
        self.PasswordItem = SensitiveItem()
        self.PrivateVaultSearchString = ''
        self.PromptForPassword = False
        self.WaitTime = 5000

