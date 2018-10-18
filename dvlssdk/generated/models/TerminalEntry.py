from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.DefaultBoolean import *
from dvlssdk.generated.enums.InternetProtocol import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.enums.PrivateKeyType import *
from dvlssdk.generated.enums.ProxyMode import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.TelnetTerminalDnsLookupType import *
from dvlssdk.generated.enums.TelnetTerminalProxyType import *
from dvlssdk.generated.enums.TerminalAutoWrap import *
from dvlssdk.generated.enums.TerminalBackspaceKeyMode import *
from dvlssdk.generated.enums.TerminalBellMode import *
from dvlssdk.generated.enums.TerminalCursorBlink import *
from dvlssdk.generated.enums.TerminalCursorKeyMode import *
from dvlssdk.generated.enums.TerminalCursorType import *
from dvlssdk.generated.enums.TerminalDisconnectAction import *
from dvlssdk.generated.enums.TerminalEncoding import *
from dvlssdk.generated.enums.TerminalFontMode import *
from dvlssdk.generated.enums.TerminalFunctionKeysMode import *
from dvlssdk.generated.enums.TerminalHomeEndKeyMode import *
from dvlssdk.generated.enums.TerminalKeypadMode import *
from dvlssdk.generated.enums.TerminalLocalEcho import *
from dvlssdk.generated.enums.TerminalLogMode import *
from dvlssdk.generated.enums.TerminalLogOverwriteMode import *
from dvlssdk.generated.enums.TerminalMouseClickMode import *
from dvlssdk.generated.enums.ToolCredentialSource import *
from dvlssdk.generated.enums.X11AuthenticationProtocol import *


class TerminalEntry:
    def __init__(self):
        self.AfterConnectMacroDelay = 500
        self.AfterConnectMacroEnterAfterCommand = True
        self.AfterConnectMacros = []
        self.AllowAgentForwarding = False
        self.AlwaysAcceptFingerprintDefaultBoolean = DefaultBoolean(0)
        self.AlwaysAskForPassword = False
        self.AutoWrap = TerminalAutoWrap(0)
        self.BackspaceKeyMode = TerminalBackspaceKeyMode(0)
        self.BeforeDisconnectMacroDelay = 500
        self.BeforeDisconnectMacroEnterAfterCommand = True
        self.BeforeDisconnectMacros = []
        self.BellMode = TerminalBellMode(0)
        self.CloseOnDisconnect = False
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.CursorBlink = TerminalCursorBlink(0)
        self.CursorKeyMode = TerminalCursorKeyMode(0)
        self.CursorType = TerminalCursorType(0)
        self.DisableKeypadMode = DefaultBoolean(0)
        self.DisconnectAction = TerminalDisconnectAction(0)
        self.Domain = ''
        self.DoubleClickDelimiters = ''
        self.EnableLogging = False
        self.EnableTCPKeepalives = False
        self.Encoding = TerminalEncoding(0)
        self.FontMode = TerminalFontMode(0)
        self.ForceNonDestructiveBackspace = False
        self.FunctionKeysMode = TerminalFunctionKeysMode(0)
        self.GssApiAuthentication = False
        self.HideOnConnect = False
        self.HomeEndKeyMode = TerminalHomeEndKeyMode(0)
        self.Host = ''
        self.HostPort = 22
        self.ImplicitCRinLF = False
        self.ImplicitLFinCR = False
        self.InternetProtocol = InternetProtocol(0)
        self.KeypadMode = TerminalKeypadMode(0)
        self.LinkedProxyID = ''
        self.LocalEcho = TerminalLocalEcho(0)
        self.LogMode = TerminalLogMode(0)
        self.LogOverwriteMode = TerminalLogOverwriteMode(0)
        self.LogPath = ''
        self.MaxScrollbackLines = 2000
        self.MouseClickMode = TerminalMouseClickMode(0)
        self.NoShell = False
        self.OverrideTerminalName = ''
        self.PasswordItem = SensitiveItem()
        self.PortForwards = []
        self.PrivateKeyConnectionID = ''
        self.PrivateKeyData = ''
        self.PrivateKeyFileName = ''
        self.PrivateKeyPassPhraseItem = SensitiveItem()
        self.PrivateKeyPromptForPassPhrase = False
        self.PrivateKeyType = PrivateKeyType(0)
        self.PrivateVaultSearchString = ''
        self.ProxyDnsLookupType = TelnetTerminalDnsLookupType(0)
        self.ProxyExcludedHosts = ''
        self.ProxyHost = ''
        self.ProxyHostPort = 0
        self.ProxyLocalHostConnections = False
        self.ProxyMode = ProxyMode(0)
        self.ProxyPasswordItem = SensitiveItem()
        self.ProxyTelnetCommand = ''
        self.ProxyType = TelnetTerminalProxyType(0)
        self.ProxyUserName = ''
        self.ReconnectDelay = 30
        self.RemoteCommand = ''
        self.ShowLogs = False
        self.SilentMode = False
        self.SSHGatewayCredentialConnectionID = ''
        self.SSHGatewayCredentialSource = ToolCredentialSource(0)
        self.SSHGatewayHost = ''
        self.SSHGatewayPasswordItem = SensitiveItem()
        self.SSHGatewayPort = 22
        self.SSHGatewayPrivateKeyConnectionID = ''
        self.SSHGatewayPrivateKeyData = ''
        self.SSHGatewayPrivateKeyFileName = ''
        self.SSHGatewayPrivateKeyPassPhraseItem = SensitiveItem()
        self.SSHGatewayPrivateKeyPromptForPassPhrase = True
        self.SSHGatewayPrivateKeyType = PrivateKeyType(0)
        self.SSHGatewayUsername = ''
        self.TCPKeepaliveInterval = 0
        self.TryAgent = False
        self.Username = ''
        self.UseSSHGateway = False
        self.UseX11Forwarding = False
        self.Verbose = False
        self.X11AuthorityFilePath = ''
        self.X11DisplayLocation = ''
        self.X11Protocol = X11AuthenticationProtocol(0)

