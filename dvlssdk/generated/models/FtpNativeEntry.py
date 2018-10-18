from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.FtpAllowedSuite import *
from dvlssdk.generated.enums.FtpProxyType import *
from dvlssdk.generated.enums.FtpSecurityType import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.enums.PrivateKeyType import *
from dvlssdk.generated.models.SensitiveItem import *


class FtpNativeEntry:
    def __init__(self):
        self.AllowedSuite = FtpAllowedSuite(0)
        self.AlwaysAskForPassword = False
        self.CertificatePath = ''
        self.ClearCommandChannel = True
        self.CommandReplyLogEnabled = False
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Directory = ''
        self.Domain = ''
        self.FtpSshAlwaysAskForPassword = False
        self.FtpSshHost = ''
        self.FtpSshPasswordItem = SensitiveItem()
        self.FtpSshPort = 22
        self.FtpSshUserName = ''
        self.Host = ''
        self.LocalPath = ''
        self.LogPath = ''
        self.LogToFile = False
        self.PassiveMode = True
        self.PasswordItem = SensitiveItem()
        self.Port = 21
        self.PrivateKeyConnectionID = ''
        self.PrivateKeyData = ''
        self.PrivateKeyFileName = ''
        self.PrivateKeyPassPhraseItem = SensitiveItem()
        self.PrivateKeyPromptForPassPhrase = True
        self.PrivateKeyType = PrivateKeyType(0)
        self.PrivateVaultSearchString = ''
        self.ProxyBypassOnLocal = False
        self.ProxyDomain = ''
        self.ProxyPasswordItem = SensitiveItem()
        self.ProxyPort = 3128
        self.ProxyType = FtpProxyType(0)
        self.ProxyUrl = ''
        self.ProxyUserName = ''
        self.SecureTransfers = False
        self.SecurityType = FtpSecurityType(0)
        self.ShowFilesInTreeView = False
        self.ShowLocalFiles = True
        self.SSL = True
        self.TLS = True
        self.UseFtpOverSsh = False
        self.UseProxy = False
        self.Username = ''
        self.UseSshAuthenticationAgent = False
        self.VerboseLevel = 0

