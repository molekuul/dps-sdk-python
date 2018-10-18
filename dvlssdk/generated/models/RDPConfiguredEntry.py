from dvlssdk.generated.enums.AuthentificationLevel import *
from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.DefaultBoolean import *
from dvlssdk.generated.enums.KeyboardHook import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.enums.RDPApplicationExternal import *
from dvlssdk.generated.enums.RDPClientSpec import *
from dvlssdk.generated.enums.RDPGatewayCredentialsSource import *
from dvlssdk.generated.enums.RDPGatewayProfileUsageMethod import *
from dvlssdk.generated.enums.RDPGatewayUsageMethod import *
from dvlssdk.generated.enums.RDPLogOffMethod import *
from dvlssdk.generated.enums.RDPNetworkConnectionType import *
from dvlssdk.generated.enums.RDPScreenSizingMode import *
from dvlssdk.generated.enums.RDPType import *
from dvlssdk.generated.enums.RDPVersion import *
from dvlssdk.generated.enums.RDPVideoPlaybackMode import *
from dvlssdk.generated.enums.ReconnectMode import *
from dvlssdk.generated.enums.ScreenColor import *
from dvlssdk.generated.enums.ScreenSize import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.SoundHook import *


class RDPConfiguredEntry:
    def __init__(self):
        self.AdminMode = False
        self.AfterLoginDelay = 500
        self.AfterLoginExecuteProgram = False
        self.AfterLoginProgram = ''
        self.AllowBackgroundInput = False
        self.AlternateFullAddress = ''
        self.AlternateShell = ''
        self.AlwaysAskForResources = False
        self.Animations = False
        self.ApplicationExternalExternal = RDPApplicationExternal(0)
        self.AudioCaptureRedirectionMode = False
        self.AuthentificationLevel = AuthentificationLevel(0)
        self.AutoReconnection = True
        self.AzureInstanceID = 0
        self.AzureRoleName = ''
        self.BandWidthAutoDetect = True
        self.BarPinned = True
        self.Centered = False
        self.ClientSpec = RDPClientSpec(0)
        self.Compression = True
        self.ConnectionType = RDPNetworkConnectionType(0)
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.CustomHeight = 0
        self.CustomWidth = 0
        self.DesktopBackground = True
        self.DesktopComposition = False
        self.DisplayConnectionBar = True
        self.Domain = ''
        self.EnableCredSSPSupport = DefaultBoolean(0)
        self.EnableSuperPan = False
        self.FontSmoothing = False
        self.GatewayAccessToken = ''
        self.GatewayCredentialConnectionID = ''
        self.GatewayCredentialsSource = RDPGatewayCredentialsSource(0)
        self.GatewayDomain = ''
        self.GatewayHostname = ''
        self.GatewayPassword = ''
        self.GatewayPersonalConnectionID = ''
        self.GatewayPrivateVaultSearchString = ''
        self.GatewayProfileUsageMethod = RDPGatewayProfileUsageMethod(0)
        self.GatewayUsageMethod = RDPGatewayUsageMethod(0)
        self.GatewayUserName = ''
        self.Host = ''
        self.HyperVInstanceID = ''
        self.KeepAliveInterval = 0
        self.KeyboardHook = KeyboardHook(0)
        self.KeyboardLayoutStr = ''
        self.KeyboardLayoutText = ''
        self.LoadAddOnsMode = DefaultBoolean(0)
        self.LoadBalanceInfo = ''
        self.MinInputSendInterval = 100
        self.MultiMonitors = False
        self.MyDefaultCredentialConnectionID = '9F3C3BCF-068A-4927-B996-CA52154CAE3B'
        self.NetworkAutoDetect = False
        self.NetworkLevelAuthentication = False
        self.PasswordItem = SensitiveItem()
        self.PersistentBitmapCaching = True
        self.PingForGateway = False
        self.Port = 3389
        self.PrivateVaultSearchCredentialConnectionID = '88E4BE76-4C5B-4694-AA9C-D53B7E0FE0DC'
        self.PrivateVaultSearchString = ''
        self.PromptCredentialOnce = False
        self.PromptCredentials = False
        self.PublicMode = False
        self.RDPLogOffMethod = RDPLogOffMethod(0)
        self.RDPLogOffWhenDisconnecting = DefaultBoolean(0)
        self.RdpType = RDPType(0)
        self.ReconnectMode = ReconnectMode(0)
        self.RedirectDirectX = False
        self.RedirectedDrives = []
        self.RemoteApp = False
        self.RemoteApplicationCmdLine = ''
        self.RemoteApplicationProgram = ''
        self.RestrictedAdminMode = False
        self.ScreenColor = ScreenColor(0)
        self.ScreenSize = ScreenSize(0)
        self.ScreenSizingMode = RDPScreenSizingMode(0)
        self.ShellWorkingDirectory = ''
        self.ShowContentWhileDragging = True
        self.SoundHook = SoundHook(0)
        self.Span = False
        self.UseAlternateShell = False
        self.UseEnhancedSessionMode = False
        self.UseRedirectionServerName = False
        self.Username = ''
        self.UsesClipboard = True
        self.UsesDevices = False
        self.UsesHardDrives = True
        self.UsesPrinters = False
        self.UsesSerialPorts = True
        self.UsesSmartDevices = False
        self.UseWinposstr = False
        self.Version = RDPVersion(0)
        self.VideoPlaybackMode = RDPVideoPlaybackMode(0)
        self.VisualStyles = True
        self.Winposstr = ''
        self.WorkspaceId = ''

