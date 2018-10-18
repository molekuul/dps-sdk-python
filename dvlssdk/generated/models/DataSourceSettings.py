from dvlssdk.generated.enums.AddEntryMode import *
from dvlssdk.generated.enums.ClipboardAccess import *
from dvlssdk.generated.enums.DefaultBoolean import *
from dvlssdk.generated.enums.ForbiddenPasswordVerificationMode import *
from dvlssdk.generated.enums.OfflineMode import *
from dvlssdk.generated.enums.PasswordComplexityUsage import *
from dvlssdk.generated.enums.PasswordStrengthCalculator import *
from dvlssdk.generated.enums.PromptForOfflinePassword import *
from dvlssdk.generated.enums.TimeBasedConnectionUsageDays import *
from dvlssdk.generated.enums.TimeBasedConnectionUsageHours import *
from dvlssdk.generated.enums.TwoFactorAuthenticationType import *


class DataSourceSettings:
    def __init__(self):
        self.AddEntryMode = AddEntryMode(0)
        self.AllowAccessAndroidPVM = True
        self.AllowAccessAndroidRDM = True
        self.AllowAccessIOSPVM = True
        self.AllowAccessIOSRDM = True
        self.AllowAccessMacPVM = True
        self.AllowAccessMacRDM = True
        self.AllowAccessWindowsPVM = True
        self.AllowAccessWindowsRDM = True
        self.AllowAttachments = True
        self.AllowClipboardPassword = False
        self.AllowConnectionLogs = True
        self.AllowConnectionStates = True
        self.AllowCredentialRepositoryInPrivateVault = False
        self.AllowDatabaseCleanUp = True
        self.AllowLocalPasswordTemplates = False
        self.AllowLocalSpecificSettings = True
        self.AllowLocalTemplates = False
        self.AllowLogCommentsEditing = False
        self.AllowOfflineCaching = True
        self.AllowOfflineEdit = False
        self.AllowRevealPassword = True
        self.AllowSendKeyPassword = False
        self.AllowSharedPasswordTemplates = True
        self.AllowSharedTemplates = True
        self.AllowSubConnection = DefaultBoolean(0)
        self.AllowUserSpecificSettings = True
        self.AllowVirtualGroups = False
        self.AutoLockOnIdle = DefaultBoolean(0)
        self.AutoLockOnMinimize = DefaultBoolean(0)
        self.AutoLockOnStandby = DefaultBoolean(0)
        self.AutoLockOnWindowsLock = DefaultBoolean(0)
        self.AutoLockTimeOut = 0
        self.CheckMaximalVersion = False
        self.CheckMaximalVersionMac = False
        self.PVMCheckMaximalVersion = False
        self.PVMCheckMaximalVersionMac = False
        self.CheckMinimalVersion = False
        self.CheckMinimalVersionMac = False
        self.PVMCheckMinimalVersion = False
        self.PVMCheckMinimalVersionMac = False
        self.CommentMinimumLength = 0
        self.ConnectionUnsafePassword = ''
        self.DataSourceVariables = []
        self.DBID = ''
        self.DefaultHtmlWelcomePage = ''
        self.DefaultPasswordTemplate = ''
        self.DefaultTemplatePath = ''
        self.DefaultTwoFactorAuthentication = TwoFactorAuthenticationType(0)
        self.DisableAutoUpdate = False
        self.DisableAutoUpdateMac = False
        self.PVMDisableAutoUpdate = False
        self.PVMDisableAutoUpdateMac = False
        self.DisableDataSourcePassword = False
        self.DisableDragAndDrop = False
        self.DisableLocalFavorites = False
        self.DisableLocalPassword = False
        self.DisablePasswordVariable = False
        self.DisablePrivateVault = False
        self.DisableQuickConnect = False
        self.DisableRdmAgentAndJump = False
        self.DisableSharedFavorites = False
        self.DisableSharedPassword = False
        self.DisableStackTrace = False
        self.DisableToolPassword = False
        self.DisableUserSpecificSettingsPassword = False
        self.EnableConnectionAfterExpiration = False
        self.EnableConnectionStates = True
        self.EnableSynchronizationByNonAdministrators = False
        self.ExcludedTypes = []
        self.ForbiddenPasswords = []
        self.ForbiddenPasswordsCaseSensitive = False
        self.ForbiddenPasswordsVerificationMode = ForbiddenPasswordVerificationMode(0)
        self.ForceApplicationGoogleAuthentification = False
        self.ForceApplicationPasswordWindows = False
        self.ForceDataSourceTwoFactor = False
        self.ForceDefaultHtmlWelcomePage = False
        self.ForceDefaultPasswordTemplate = False
        self.HideRegistration = False
        self.IncludePrivateVaultLogs = False
        self.IsLockedDownByDefault = False
        self.JumpSerial = ''
        self.LoadCredentialsInSessions = True
        self.LoadSessionToolInSessions = True
        self.MaxFileSizeByte = 26214400
        self.MaximalMacVersionMessage = ''
        self.MaximalVersionMessage = ''
        self.PVMMaximalMacVersionMessage = ''
        self.PVMMaximalVersionMessage = ''
        self.MergeCredentialsInSessions = DefaultBoolean(0)
        self.MinimalMacVersionMessage = ''
        self.MinimalVersionMessage = ''
        self.PVMMinimalMacVersionMessage = ''
        self.PVMMinimalVersionMessage = ''
        self.PasswordClipboard = ClipboardAccess(0)
        self.PasswordComplexities = []
        self.PasswordComplexityUsage = PasswordComplexityUsage(0)
        self.PasswordConfigurationTemplates = []
        self.PasswordHistory = 5
        self.PasswordStrengthMethod = PasswordStrengthCalculator(0)
        self.PromptForOfflinePassword = PromptForOfflinePassword(0)
        self.PVMInstallerPath = ''
        self.PVMInstallerPathMac = ''
        self.PVMMaximalVersion = ''
        self.PVMMaximalVersionMac = ''
        self.PVMMinimalVersion = ''
        self.PVMMinimalVersionMac = ''
        self.ResolveCredentialsInOverview = True
        self.RDMInstallerPath = ''
        self.RDMInstallerPathMac = ''
        self.RDMMaximalVersion = ''
        self.RDMMaximalVersionMac = ''
        self.RDMMinimalVersion = ''
        self.RDMMinimalVersionMac = ''
        self.SecurityProviderName = ''
        self.SecurityProviderSettings = ''
        self.SelectedDayOfWeek = 0
        self.SelectedTimeZoneId = ''
        self.Serial = ''
        self.SystemMessage = ''
        self.TimeBasedUsageDays = TimeBasedConnectionUsageDays(0)
        self.TimeBasedUsageEndTime = ''
        self.TimeBasedUsageHours = TimeBasedConnectionUsageHours(0)
        self.TimeBasedUsageStartTime = ''
        self.UseRoleSecurity = True
        self.AllowOfflineMode = True
        self.ConnectionCacheID = ''
        self.Custom = None
        self.IntelligentCacheID = ''
        self.MaxFileSizeKByte = 0
        self.MaxFileSizeMByte = 0
        self.OfflineMode = OfflineMode(0)
        self.OfflineModeExpiration = 7
        self.Permissions = []

