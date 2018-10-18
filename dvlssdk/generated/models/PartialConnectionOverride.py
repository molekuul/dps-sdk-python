from dvlssdk.generated.enums.ConnectionDisplayMode import *
from dvlssdk.generated.models.CredentialUsernamePassword import *
from dvlssdk.generated.enums.DefaultBoolean import *
from dvlssdk.generated.enums.DisplayMonitor import *
from dvlssdk.generated.models.JumpConnection import *
from dvlssdk.generated.enums.KeyboardHook import *
from dvlssdk.generated.enums.PrivateKeyType import *
from dvlssdk.generated.enums.RDPScreenSizingMode import *
from dvlssdk.generated.enums.ScreenSize import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.WebBrowserApplication import *


class PartialConnectionOverride:
    def __init__(self):
        self.ConnectionID = None
        self.CredentialConnectionID = ''
        self.Credentials = CredentialUsernamePassword()
        self.CustomHeight = 0
        self.CustomWidth = 0
        self.Display = ConnectionDisplayMode(0)
        self.DisplayMonitor = DisplayMonitor(0)
        self.Domain = ''
        self.GatewayCredentialConnectionID = ''
        self.GatewayDomain = ''
        self.GatewayPassword = ''
        self.GatewayPersonalConnectionID = ''
        self.GatewayUserName = ''
        self.Jump = JumpConnection()
        self.KeyboardHook = KeyboardHook(0)
        self.OverrideCredential = False
        self.OverrideDisplay = False
        self.OverrideGateway = False
        self.OverrideJump = False
        self.OverrideKeyboardHook = False
        self.OverrideMore = False
        self.OverridePrinters = False
        self.OverridePrivateKey = False
        self.OverrideResources = False
        self.OverrideScreenSize = False
        self.OverrideToolCredential = False
        self.OverrideVPNCredential = False
        self.OverrideWebBrowserApplication = False
        self.Password = ''
        self.PersonalCredentialConnectionID = ''
        self.PinEmbeddedMode = DefaultBoolean(0)
        self.PrivateKeyConnectionID = ''
        self.PrivateKeyData = ''
        self.PrivateKeyFileName = ''
        self.PrivateKeyOverrideUsername = ''
        self.PrivateKeyPassPhraseItem = SensitiveItem()
        self.PrivateKeyPromptForPassPhrase = True
        self.PrivateKeyType = PrivateKeyType(0)
        self.RDPScreenSizingMode = RDPScreenSizingMode(0)
        self.RedirectedDrives = []
        self.ScreenSize = ScreenSize(0)
        self.ToolCredentialConnectionGroup = ''
        self.ToolCredentialConnectionID = ''
        self.ToolDomain = ''
        self.ToolPassword = ''
        self.ToolPersonalConnectionID = ''
        self.ToolUserName = ''
        self.UserName = ''
        self.UsesHardDrives = False
        self.UsesPrinters = False
        self.VPNCredentialConnectionGroup = ''
        self.VPNCredentialConnectionID = ''
        self.VPNDomain = ''
        self.VPNPassword = ''
        self.VPNPersonalConnectionID = ''
        self.VPNUserName = ''
        self.WebBrowserApplication = WebBrowserApplication(0)

