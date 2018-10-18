from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.enums.ProxyTunnelType import *
from dvlssdk.generated.models.SensitiveItem import *


class ProxyTunnelEntry:
    def __init__(self):
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.LocalHost = ''
        self.LocalPort = 1
        self.PasswordItem = SensitiveItem()
        self.PrivateVaultSearchString = ''
        self.ProxyHost = ''
        self.ProxyPort = 80
        self.ProxyType = ProxyTunnelType(0)
        self.RemoteHost = ''
        self.RemotePort = 1
        self.Username = ''

