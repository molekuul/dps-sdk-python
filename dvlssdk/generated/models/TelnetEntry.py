from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.InternetProtocol import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.TelnetTerminalDnsLookupType import *
from dvlssdk.generated.enums.TelnetTerminalProxyType import *
from dvlssdk.generated.enums.TerminalLogMode import *
from dvlssdk.generated.enums.TerminalLogOverwriteMode import *


class TelnetEntry:
    def __init__(self):
        self.AlwaysAskForPassword = False
        self.CloseOnDisconnect = True
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Domain = ''
        self.DoubleClickDelimiters = ''
        self.EnableLogging = False
        self.Host = ''
        self.HostPort = 23
        self.InternetProtocol = InternetProtocol(0)
        self.LogMode = TerminalLogMode(0)
        self.LogOverwriteMode = TerminalLogOverwriteMode(0)
        self.LogPath = ''
        self.PasswordDelay = 1000
        self.PasswordItem = SensitiveItem()
        self.PrivateVaultSearchString = ''
        self.ProxyDnsLookupType = TelnetTerminalDnsLookupType(0)
        self.ProxyExcludedHosts = ''
        self.ProxyHost = ''
        self.ProxyLocalHostConnections = False
        self.ProxyPasswordItem = SensitiveItem()
        self.ProxyPort = 80
        self.ProxyTelnetCommand = ''
        self.ProxyType = TelnetTerminalProxyType(0)
        self.ProxyUsername = ''
        self.SilentMode = False
        self.Username = ''
        self.Verbose = False

