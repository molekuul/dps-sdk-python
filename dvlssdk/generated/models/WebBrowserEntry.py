from dvlssdk.generated.enums.BrowserExtensionLinkerCompareType import *
from dvlssdk.generated.enums.ChromeProxyType import *
from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.DefaultBoolean import *
from dvlssdk.generated.enums.MozillaManualProxyConfigurationProxyType import *
from dvlssdk.generated.enums.MozillaNetworkProxyType import *
from dvlssdk.generated.enums.OTPCodeSize import *
from dvlssdk.generated.enums.OTPHashAlgorithm import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.WebBrowserApplication import *
from dvlssdk.generated.enums.WebBrowserAuthenticationMode import *
from dvlssdk.generated.enums.WebBrowserSubApplication import *


class WebBrowserEntry:
    def __init__(self):
        self.AlwaysLaunchOnProtocolRequest = False
        self.AuthenticationMode = WebBrowserAuthenticationMode(0)
        self.AutoFillLogin = False
        self.AutomaticRefresh = False
        self.AutomaticRefreshTime = 0
        self.AutoSubmit = False
        self.BrowserExtensionLinkerCompareType = BrowserExtensionLinkerCompareType(0)
        self.ChromeProxyType = ChromeProxyType(0)
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.CustomAutoFillHtmlItems = []
        self.CustomJavaScript = ''
        self.DelayedRefreshTime = 0
        self.DisableAutomation = False
        self.Domain = ''
        self.DomainControlId = ''
        self.EnableKeyboardShortcuts = False
        self.EnableWebBrowserExtension = False
        self.Force32Bit = False
        self.ForceHttps = False
        self.FormId = ''
        self.Host = ''
        self.IgnoreCertificateAuthentication = False
        self.IgnoreCertificateErrors = False
        self.LanguageCode = ''
        self.MobileDomainControlId = ''
        self.MobileFormId = ''
        self.MobileOTPControlId = ''
        self.MobilePasswordControlId = ''
        self.MobileSubmitControlId = ''
        self.MobileUserNameControlId = ''
        self.MozillaManualProxyConfigurationProxyType = MozillaManualProxyConfigurationProxyType(0)
        self.MozillaProxyType = MozillaNetworkProxyType(0)
        self.NoMerge = False
        self.OTPCodeSize = OTPCodeSize(0)
        self.OTPControlId = ''
        self.OTPCredentialId = ''
        self.OTPHashAlgorithm = OTPHashAlgorithm(0)
        self.OTPKey = ''
        self.OTPTimeStep = 30
        self.PasswordControlId = ''
        self.PasswordItem = SensitiveItem()
        self.PrivateSession = False
        self.PrivateVaultSearchString = ''
        self.ProxyExcludedList = ''
        self.ProxyPort = 0
        self.ProxyUrl = ''
        self.RegularExpression = ''
        self.ScriptErrorsSuppressed = False
        self.SecurityAnswer1Item = SensitiveItem()
        self.SecurityAnswer2Item = SensitiveItem()
        self.SecurityAnswer3Item = SensitiveItem()
        self.SecurityAnswer4Item = SensitiveItem()
        self.SecurityAnswer5Item = SensitiveItem()
        self.SecurityQuestion1 = ''
        self.SecurityQuestion2 = ''
        self.SecurityQuestion3 = ''
        self.SecurityQuestion4 = ''
        self.SecurityQuestion5 = ''
        self.ShowFavicon = True
        self.ShowToolbar = True
        self.ShowUrl = True
        self.SubmitControlId = ''
        self.Url = ''
        self.UseLegacyClick = DefaultBoolean(0)
        self.Username = ''
        self.UserNameControlId = ''
        self.WebBrowserApplication = WebBrowserApplication(0)
        self.WebBrowserSubApplication = WebBrowserSubApplication(0)

