from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *


class HostEntry:
    def __init__(self):
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Domain = ''
        self.Host = ''
        self.PasswordItem = SensitiveItem()
        self.PromptForHost = False
        self.Username = ''
        self.UseTemplateCredentials = False
        self.UseTemplateHost = False

