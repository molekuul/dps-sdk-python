from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.KeyboardHook import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.VNCColorDepth import *
from dvlssdk.generated.enums.VNCCursorMode import *
from dvlssdk.generated.enums.VNCEmbeddedType import *
from dvlssdk.generated.enums.VNCEncoding import *
from dvlssdk.generated.enums.VNCType import *


class VNCEntry:
    def __init__(self):
        self.ConfigFileName = ''
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.CustomCompressionLevel = 6
        self.DisableClipboard = False
        self.Domain = ''
        self.DSM = ''
        self.EmbeddedConfiguration = ''
        self.EmbeddedDelayx64Only = -1
        self.EmulateThreeButton = True
        self.FullScreen = False
        self.HideToolStrip = False
        self.Host = ''
        self.JPEGCompressionLevel = 6
        self.KeyboardHook = KeyboardHook(0)
        self.MouseCursorMode = VNCCursorMode(0)
        self.OtherParameters = ''
        self.PasswordItem = SensitiveItem()
        self.Port = 5900
        self.PreferredEncoding = VNCEncoding(0)
        self.PrivateVaultSearchString = ''
        self.ProxyHost = ''
        self.RequestSharedSession = True
        self.Scaled = True
        self.ScreenColorDepth = VNCColorDepth(0)
        self.ShowStatus = True
        self.SwapMouseButtons = False
        self.TrackMouseMovement = True
        self.Username = ''
        self.ViewOnly = False
        self.VncEmbeddedType = VNCEmbeddedType(0)
        self.VNCPasswordItem = SensitiveItem()
        self.VNCType = VNCType(0)

