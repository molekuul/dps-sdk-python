from dvlssdk.generated.enums.ARDSessionSelectRequestType import *
from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.KeyboardHook import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.VNCAuthentificationType import *
from dvlssdk.generated.enums.VNCCursorMode import *
from dvlssdk.generated.enums.VNCEncoding import *
from dvlssdk.generated.enums.VNCSelectDisplayMode import *


class AppleRemoteDesktopEntry:
    def __init__(self):
        self.ARDSessionSelectRequestType = ARDSessionSelectRequestType(0)
        self.AuthentificationType = VNCAuthentificationType(0)
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.CustomCompressionLevel = 6
        self.DisableClipboard = False
        self.Domain = ''
        self.EmulateThreeButton = True
        self.Host = ''
        self.KeyboardHook = KeyboardHook(0)
        self.MouseCursorMode = VNCCursorMode(0)
        self.PasswordItem = SensitiveItem()
        self.Port = 5900
        self.PreferredEncoding = VNCEncoding(0)
        self.PrivateVaultSearchString = ''
        self.RequestSharedSession = True
        self.Scaled = True
        self.SelectDisplayIndex = 0
        self.SelectDisplayMode = VNCSelectDisplayMode(0)
        self.SwapMouseButtons = False
        self.Username = ''
        self.ViewOnly = False

