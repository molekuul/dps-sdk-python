from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.enums.PrivateKeyType import *
from dvlssdk.generated.enums.ProxyTunnelType import *
from dvlssdk.generated.models.SensitiveItem import *


class WebDavEntry:
    def __init__(self):
        self.AlwaysAskForPassword = False
        self.CommandReplyLogEnabled = False
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Directory = ''
        self.Domain = ''
        self.HomeDirectory = ''
        self.Host = ''
        self.LocalPath = ''
        self.LogPath = ''
        self.LogToFile = False
        self.PasswordItem = SensitiveItem()
        self.Port = 80
        self.PrivateKeyConnectionID = ''
        self.PrivateKeyData = ''
        self.PrivateKeyFileName = ''
        self.PrivateKeyPassPhraseItem = SensitiveItem()
        self.PrivateKeyType = PrivateKeyType(0)
        self.PrivateVaultSearchString = ''
        self.ProxyBypassOnLocal = False
        self.ProxyDomain = ''
        self.ProxyHost = ''
        self.ProxyPasswordItem = SensitiveItem()
        self.ProxyPort = 0
        self.ProxyType = ProxyTunnelType(0)
        self.ProxyUserName = ''
        self.ShowFilesInTreeView = False
        self.ShowLocalFiles = False
        self.SshAlwaysAskForPassword = False
        self.SshHost = ''
        self.SshPasswordItem = SensitiveItem()
        self.SshPort = 0
        self.SshUserName = ''
        self.UseProxy = False
        self.Username = ''
        self.UseSshAuthenticationAgent = False
        self.UseSsl = False
        self.UseWebDavOverSsh = False
        self.VerboseLevel = 0

