from dvlssdk import DVLSConnection
from dvlssdk import ApiTesting
import string
import random
import datetime
import logging
import sys
from dvlssdk import ConnectionType
from dvlssdk.generated.enums.CheckOutMode import CheckOutMode
from dvlssdk.generated.enums.CommandLineCaptureOutputMode import CommandLineCaptureOutputMode
from dvlssdk.generated.enums.CredentialMode import CredentialMode
from dvlssdk.generated.enums.CommandLineExecutionMode import CommandLineExecutionMode
from dvlssdk.generated.enums.PasswordComplexityValidation import PasswordComplexityValidation
from dvlssdk.generated.enums.PasswordGeneratorMode import PasswordGeneratorMode

# Constants
# DVLS_DB_Zip = "./../tests/EntryList.zip"
# DVLS_URI = 'http://127.0.0.1/dvlsSDK'
DVLS_URI = 'http://127.0.0.1/dpsDatabaseDLL'
DVLS = DVLSConnection(DVLS_URI, errorLevelLog='INFO')
DVLS_ADMIN_USER = 'mainuser'
DVLS_ADMIN_PW = '123456'
DVLS_EXISTING_DOMAIN_USERS = ['ted@windjammer.loc',
                              'ted',
                              'WINDJAMMER\\ted',
                              'dan@windjammer.loc',
                              'victor@downhillpros.com',
                              'william.fox@windjammer.loc',
                              'burton.guido@downhillpros.com']
# To test logging in using a wrong domain
DVLS_NON_EXISTING_DOMAIN_USER = 'AJUZUZ\\ted'
DVLS_NEW_CUSTOM_USERS = ['_Bill',
                         '_Ted']
DVLS_NEW_CUSTOM_USERS_PW = '123456'
DVLS_WRONG_PW = '654321'

DVLS_NEW_ROLES = ['SA',
                  'RH']
ALL_ROLES = ['SA',
             'SAb',
             'RH',
             'RHb']
DVLS_NEW_REPOSITORIES = ['Repo1',
                         'Repo2']
DVLS_SEC_GROUPS = ['SG1',
                   'SG2']

ALL_SEC_GROUPS = ['SG1',
                  'SG1b',
                  'SG2',
                  'SG2b']

ST_ENTRIES = DVLS.STANDARD_ENTRY_TYPES
CT_ENTRIES = DVLS.CONTACT_ENTRY_TYPES
DT_ENTRIES = DVLS.DATA_ENTRY_TYPES
NO_DISPLAY = False

TIME_CURRENT = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute)
TIME_IN_ONE_HOUR = str(datetime.datetime.now().hour + 1) + ':' + str(datetime.datetime.now().minute)
TOMORROW = str(datetime.datetime.now() + datetime.timedelta(1))

def _set_logger(logger, log_level):
    try:
        log_level = getattr(logging, log_level.upper())
    except AttributeError:
        log_level = getattr(logging, 'INFO')
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    console_handler.setFormatter(console_formatter)

    file_handler = logging.handlers.RotatingFileHandler('TestResult.log', mode='a', maxBytes=2000024, backupCount=5)
    file_handler.setLevel(log_level)
    file_formatter = logging.Formatter("%(asctime)s [%(name)s] -- %(message)s")
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

TestLogger = logging.getLogger('dvlssdk.Tests.Full')
_set_logger(TestLogger, logging.DEBUG)

def delete_entries(result):
    if result.success:
        entries = result.data
        if entries.__len__() > 0:
            DVLS.delete_entry_by_id(entries[0]['id'], NO_DISPLAY)

def run_cleanup():
    DVLS.dvls_logger.info("# Delete roles #", NO_DISPLAY)
    for role in ALL_ROLES:
        DVLS.delete_role_by_name(role, NO_DISPLAY)

    DVLS.dvls_logger.info("# Delete Security Groups #", NO_DISPLAY)
    for group in ALL_SEC_GROUPS:
        DVLS.delete_security_group_by_name(group, NO_DISPLAY)

    DVLS.dvls_logger.info("# Delete Users #", NO_DISPLAY)
    for user in DVLS_NEW_CUSTOM_USERS:
        DVLS.delete_user_by_name(user, NO_DISPLAY)
    for user in DVLS_EXISTING_DOMAIN_USERS:
        DVLS.delete_user_by_name(user, NO_DISPLAY)

    DVLS.dvls_logger.info("# Delete entries #", NO_DISPLAY)

    delete_entries(DVLS.get_connections_by_name("SSH Tunnel Entry", DEFAULT_REPO_ID, NO_DISPLAY))
    delete_entries(DVLS.get_connections_by_name("Credential Entry", DEFAULT_REPO_ID, NO_DISPLAY))
    delete_entries(DVLS.get_connections_by_name("Command Line Entry", DEFAULT_REPO_ID, NO_DISPLAY))
    delete_entries(DVLS.get_connections_by_name("RDP Configured Entry", DEFAULT_REPO_ID, NO_DISPLAY))
    delete_entries(DVLS.get_connections_by_name("SSH Shell Entry", DEFAULT_REPO_ID, NO_DISPLAY))
    delete_entries(DVLS.get_connections_by_name("Default Repository - Private Key Entry", DEFAULT_REPO_ID, NO_DISPLAY))
    delete_entries(DVLS.get_connections_by_name("Group Entry", DEFAULT_REPO_ID, NO_DISPLAY))
    delete_entries(DVLS.get_connections_by_name("Group Entry 2", DEFAULT_REPO_ID, NO_DISPLAY))

    result = DVLS.get_private_vault_entries_by_name("Private Vault - Private Key Entry", NO_DISPLAY)
    if result.success:
        entries = result.data
        if entries.__len__() > 0:
            DVLS.delete_private_vault_entry_by_id(entries[0]['id'], NO_DISPLAY)

    result = DVLS.get_password_templates(NO_DISPLAY)
    if result.success:
        templates = result.data
        for template in templates:
            DVLS.delete_password_template_by_id(template.get('id'), NO_DISPLAY)

    for repo in DVLS_NEW_REPOSITORIES:
         DVLS.delete_repository_by_name(repo, NO_DISPLAY)


TestLogger.info("---------------------------------------------------------------------------------------------\n")
TestLogger.info("           ######################")
TestLogger.info("           ### CRITICAL TESTS ###")
TestLogger.info("           ######################")
TestLogger.info(" ")
DVLS.login(DVLS_ADMIN_USER, DVLS_ADMIN_PW)
users_result = DVLS.get_users(NO_DISPLAY)
users = 1
if users_result.success:
    users = len(users_result.data)
DVLSTest = ApiTesting.ApiTesting(DVLS, TestLogger, users)

DEFAULT_REPO_ID = DVLS.get_repository_id("Default", NO_DISPLAY).data

run_cleanup()

TestLogger.info(" ")
TestLogger.info("           # Create roles #")
TestLogger.info("           ----------------------------------------")
for role in DVLS_NEW_ROLES:
    DVLSTest.create_role_test(role)

TestLogger.info(" ")
TestLogger.info("           # Create Security Groups #")
TestLogger.info("           ----------------------------------------")
for group in DVLS_SEC_GROUPS:
    DVLSTest.create_security_group_test(group, Description=group + ' description')

TestLogger.info(" ")
TestLogger.info("           # Create Users #")
TestLogger.info("           ----------------------------------------")

role_RH_id = ''
role_RH_result = DVLS.get_role_id('RH', NO_DISPLAY)
if role_RH_result.success:
    role_RH_id = role_RH_result.data

role_SA_id = ''
role_SA_result = DVLS.get_role_id('SA', NO_DISPLAY)
if role_SA_result.success:
    role_SA_id = role_SA_result.data

for user in DVLS_NEW_CUSTOM_USERS:
    eMail = 'new' + ''.join(random.SystemRandom().choice(string.digits)
                            for _ in range(5)) + '@dvls.com'
    DVLSTest.create_user_test(
                user,
                'Builtin',
                DVLS_NEW_CUSTOM_USERS_PW,
                Email=eMail,
                GravatarEmail=eMail,
                HasAccessPVM=True,
                HasAccessRDM=True,
                HasAccessWeb=True,
                HasAccessWebLogin=True,
                CustomRoles=[role_RH_id],
                AllowDragAndDrop=True,
                AllowRevealPassword=True,
                CanExport=True,
                CanImport=True,
                CanViewDetails=True,
                CanViewGlobalLogs=True,
                CanViewInformations=True,
                OfflineMode='ReadWrite')

for user in DVLS_EXISTING_DOMAIN_USERS:
    eMail = 'new' + ''.join(random.SystemRandom().choice(string.digits)
                            for _ in range(5)) + '@domain.com'
    DVLSTest.create_user_test(
                user,
                'Domain',
                None,
                Email=eMail,
                GravatarEmail=eMail,
                HasAccessPVM=False,
                HasAccessRDM=False,
                HasAccessWeb=True,
                HasAccessWebLogin=False,
                CustomRoles=[role_SA_id],
                AllowDragAndDrop=False,
                AllowRevealPassword=False,
                CanExport=False,
                CanImport=False,
                CanViewDetails=False,
                CanViewGlobalLogs=False,
                CanViewInformations=False,
                OfflineMode='ReadOnly')

sec_group0 = 0
sec_group_result = DVLS.get_security_group_id(DVLS_SEC_GROUPS[0], NO_DISPLAY)
if sec_group_result.success:
    sec_group0 = sec_group_result.data

sec_group1 = 0
sec_group_result = DVLS.get_security_group_id(DVLS_SEC_GROUPS[1], NO_DISPLAY)
if sec_group_result.success:
    sec_group1 = sec_group_result.data

DVLSTest.get_users_test()

DVLSTest.login_test(DVLS_ADMIN_USER, DVLS_ADMIN_PW)

TestLogger.info(" ")
TestLogger.info("           # Create repositories #")
for repo in DVLS_NEW_REPOSITORIES:
    DVLSTest.create_repository_test(repo, Description=repo + ' description')

TestLogger.info(" ")
TestLogger.info("           # Change repository #")
DVLSTest.change_repository_test(DVLS_NEW_REPOSITORIES[0], 1)

DVLS.change_repository("Default", NO_DISPLAY)

TestLogger.info(" ")
TestLogger.info("           # Delete repositories #")

for repo in DVLS_NEW_REPOSITORIES:
    DVLSTest.delete_repository_test(repo)

TestLogger.info(" ")
TestLogger.info("           # Create password template #")
TestLogger.info("           ----------------------------------------")

DVLSTest.create_password_template_test(PasswordGeneratorMode.SpecifiedSettings,
                                        "Password Configuration Entry",
                                       BracketsMin=1,
                                       CustomCharacters="@#$%&!",
                                       CustomCharactersMin=2,
                                       CustomExcludeCharacters="^¨`~°",
                                       DigitsMin=3,
                                       HighAnsiMin=4,
                                       Length=100,
                                       LowerCaseMin=5,
                                       MinusMin=6,
                                       PreviewPasswordCount=7,
                                       SpaceMin=8,
                                       SpecialCharMin=9,
                                       UnderlineMin=10,
                                       UpperCaseMin=11,
                                       XmlCompliant=True)

TestLogger.info(" ")
TestLogger.info("           # Modify features #")
TestLogger.info("           ----------------------------------------")

DVLSTest.modify_features_test(AllowBrowserExtension = True,
                                    ApiHelpPageEnabled = True,
                                    ProxyEnabled = True)

DVLSTest.modify_features_test(AllowBrowserExtension = False,
                                    ApiHelpPageEnabled = False,
                                    ProxyEnabled = False)

TestLogger.info(" ")
TestLogger.info("           # Create entries #")
TestLogger.info("           ----------------------------------------")
DVLSTest.create_connection_test("Group Entry",
                                ConnectionType.Group,
                                Description="Group Entry Description",
                                Keywords='Tag1 Tag2')

DVLSTest.create_connection_test(
            "Group Entry 2",
            ConnectionType.Group,
            Description="Group Entry 2 Description",
            Group='Group Entry',
            Keywords='Tag1 Tag2')

DVLSTest.create_connection_test(
            "Command Line Entry",
            ConnectionType.CommandLine,
            CaptureOutputMode=CommandLineCaptureOutputMode.File.value,
            CaptureOutputFilePath='CapOutFilePath',
            CommandLine='CommandLineRun',
            CommandLineWaitForApplicationToExit=True,
            CredentialSource='Custom',
            CredentialConnectionId='CredConId',
            CredentialConnectionID='CredConID',
            Description='Description',
            Domain='Domain',
            EmbeddedWaitTime=500,
            ExecutionMode=CommandLineExecutionMode.Capture.value,
            Expiration=str(datetime.datetime.now()
                          + datetime.timedelta(1)),
            Group='Group Entry',
            Host='Host',
            Keywords='Tag1 Tag2',
            NetOnly=True,
            Parameter1DataType='Secured',
            Parameter1DefaultValue='P1Default',
            Parameter1Label='P1Label',
            Password='Password',
            ProcessName='CommandLineRun',
            Run64BitsMode=True,
            RunAsAdministrator=True,
            RunAsDomain='Domain',
            RunAsPassword='Password',
            RunAsPromptForCredentials=True,
            RunAsUsername='Username',
            UserName='Username')

DVLSTest.create_credential_test("Default",
                                "Credential Entry",
                                UserName='UserName',
                                Password='Password',
                                Domain='Domain',
                                MnemonicPassword='MnemonicPassword')

DVLSTest.create_credential_test("PrivateKey", "Default Repository - Private Key Entry")

DVLSTest.create_credential_test("PrivateKey", "Private Vault - Private Key Entry", IsPrivate=True)

cred_entry_result = DVLS.get_connections_by_name('Credential Entry', DEFAULT_REPO_ID, NO_DISPLAY)
cred_entry_id = ''
if cred_entry_result.success:
    cred_entry_id = cred_entry_result.data[0]['id']

private_vault_key_id = ''
private_vault_keys_result = DVLS.get_private_vault_entries_by_name("Private Vault - Private Key Entry", NO_DISPLAY)
if private_vault_keys_result.success:
    private_vault_key_id = private_vault_keys_result.data[0]['id']

password_template_id = ''
password_template_result = DVLS.get_password_templates_by_name("Password Configuration Entry", NO_DISPLAY)
if password_template_result.success:
    password_template_id = password_template_result.data[0]['id']

DVLSTest.create_connection_test(
            "RDP Configured Entry",
            ConnectionType.RDPConfigured,
            AdminMode=True,
            AfterLoginDelay=1000,
            AfterLoginExecuteProgram=True,
            AfterLoginProgram='AftLoginPgm',
            AllowBackgroundInput=True,
            AllowOffline='true',
            AlternateFullAddress='AltFullAdress',
            AlternateShell='AltShell',
            Animations=True,
            AudioCaptureRedirectionMode=True,
            AuthentificationLevel='WarnMe',
            AutoReconnection=False,
            BandWidthAutoDetect=False,
            BarPinned=False,
            # Centered=True,
            ConnectionType='LAN',
            Compression=False,
            CredentialMode=CredentialMode.Default.value,
            CustomHeight=1,
            CustomWidth=1,
            CheckOutMode=CheckOutMode.Automatic.value,
            Delete='Never',
            Description='RDP Configured Description',
            DesktopBackground=False,
            DesktopComposition=True,
            DisplayConnectionBar=False,
            Domain='Domain',
            Edit='Everyone',
            EditAttachment='Never',
            EditSecurity='Default',
            EnableCredSSPSupport='true',
            EnableSuperPan=True,
            Expiration=TOMORROW,
            FontSmoothing=True,
            GatewayProfileUsageMethod='Explicit',
            # 'Default' -> Use GatewayUsageMethod='ProxyModeDetect'
            # 'Explicit' -> Different GatewayUsageMethod.
            GatewayUsageMethod='ModeDirect',
            # 'NoneDetect' = Do not use RD Gateway server.  'ProxyModeDetect' = Bypass local. 'ModeDirect' = No bypass local. Other settings are not used.
            # GatewayAccessToken='GWAccTok',
            GatewayCredentialConnectionID=cred_entry_id,
            GatewayCredentialsSource='AskMeLater',
            # Available values; 'UserPassword', 'Smartcard', 'AskMeLater' or 'GatewayAccessToken'
            # GatewayDomain='GWdom',
            GatewayHostname='GWHostname',
            # GatewayPassword='GWpw', #Only specify password if it needs to be saved in the database, otherwise it is saved locally
            # GatewayPersonalConnectionID='GWpersoConID',
            # GatewayPrivateVaultSearchString='GWprvVltSrchStr',
            # GatewayUseCredRepoPrompt=True,
            # GatewayUsePersoCred=True,
            # GatewayUserName='GWusrName',
            Group='Group Entry\Group Entry 2',
            Host='Host',
            Inventory='Default',
            KeepAliveInterval=10,
            KeyboardHook='InFullScreenMode',
            Keywords='Tag1 Tag2',
            LoadAddOnsMode='true',
            LoadBalanceInfo='LoadBalInfo',
            MinInputSendInterval=200,
            NetworkAutoDetect=True,
            NetworkLevelAuthentication=True,
            MinimumLengthCount=1,  # For Password Validation
            MinimumLowerCaseCount=1,  # For Password Validation
            MinimumNumericCount=1,  # For Password Validation
            MinimumSymbolCount=1,  # For Password Validation
            MinimumUpperCaseCount=1,  # For Password Validation
            MultiMonitors=True,
            Password='Password',
            PasswordTemplateId=password_template_id,
            # Default = '', Other possible values = 'Inherited', 'None', and 'NameOfTemplate'
            PasswordValidationUsage=PasswordComplexityValidation.Inherited.value,
            PersistentBitmapCaching=False,
            PingForGateway=True,
            Port=1,
            PromptCredentials=True,
            PublicMode=True,
            RDPLogOffMethod='RDMAgent',
            RDPLogOffWhenDisconnecting='true',
            RdpVersion='RDP60',
            ReconnectMode='SmartReconnect',
            RedirectDirectX=True,
            RestrictedAdminMode=True,
            RemoteApp=True,
            RemoteApplicationCmdLine='RemAppCmdLine',
            RemoteApplicationProgram='RemAppPgm',
            RequireCheckOutMode='false',
            # RoleOverride='Everyone', #'Default', 'Everyone' or 'Never'
            ScreenColor='C16Bits',
            ScreenSize='Custom',
            ScreenSizingMode='FitToWindow',
            SecurityGroup=DVLS_SEC_GROUPS[0],
            ShellWorkingDirectory='ShellWrkDir',
            ShowContentWhileDragging=False,
            SortPriority=1,
            SoundHook='DoNotPlay',
            Span=True,
            TimeBasedUsageDays="Sun-Mon-Tue-Wed-Thu-Fri-Sat",
            # 'WeekEnds', 'Inherited'
            # TimeBasedUsageHours='Inherited',
            TimeBasedUsageTimePeriod=TIME_CURRENT + '-'
                                    + TIME_IN_ONE_HOUR,
            UseAlternateShell=True,
            UserName='Username',
            UsesClipboard=False,
            UsesDevices=True,
            UsesHardDrives=False,
            UsesPrinters=True,
            UseRedirectionServerName=True,
            UsesSerialPorts=False,
            UsesSmartDevices=True,
            VideoPlaybackMode='Default',
            VisualStyles=False,
            WinPostStr='WinPostStr',
            WorkspaceId='WKSPCID')

DVLSTest.create_connection_test(
            "SSH Tunnel Entry",
            ConnectionType.SSHTunnel,
            AllowAgentForwarding=True,
            AllowOffline='true',
            AlwaysAskForPassword=True,
            AlwaysAcceptFingerprintDefaultBoolean='true',
            CheckOutMode=CheckOutMode.Automatic.value,
            Destination='RemoteHost',
            DestinationPort=1,
            DisconnectAction='KeepOpen',
            EnableLogging=True,
            EnableTCPKeepalives=True,
            Expiration=TOMORROW,
            Group='Group Entry\Group Entry 2',
            GssApiAuthentication=True,
            HideOnConnect=True,
            Host='Host',
            HostPort=21,
            InternetProtocol='IPv4',
            Keywords="Tag1 Tag2",
            LogPath='LogPath',
            NoShell=True,
            Password='Password',
            PasswordTemplateId=password_template_id,
            PasswordValidationUsage='Inherited',
            # PrivateKeyConnectionID='Default Repository - Private Key Entry',
            # PrivateKeyData='PrivateKeyData',
            # PrivateKeyFileName="./../tests/Data.ppk",
            PrivateKeyType='MyDefault',
            ReconnectDelay=20,
            RequireCheckOutMode='false',
            SecurityGroup=DVLS_SEC_GROUPS[0],
            ShowLogs=True,
            SilentMode=True,
            Source='LocalAddress',
            SourcePort=1,
            TCPKeepaliveInterval=6,
            TimeBasedUsageDays="Sun-Mon-Tue-Wed-Thu-Fri-Sat",
            TimeBasedUsageTimePeriod=TIME_CURRENT + '-'
                                    + TIME_IN_ONE_HOUR,
            TryAgent=True,
            UserName='Username',
            UseSSHGateway=True,
            Verbose=True)

DVLSTest.create_connection_test(
            "SSH Shell Entry",
            ConnectionType.SSHShell,
            AfterConnectMacroDelay=100,
            AfterConnectMacroEnterAfterCommand=False,
            AfterConnectMacros=["A", "B", "C", "D", "E", "F\nG\nH"],
            AllowAgentForwarding=True,
            AlwaysAcceptFingerprintDefaultBoolean='false',
            AlwaysAskForPassword=True,
            AutoWrap='Off',
            BackspaceKeyMode='ControlQuestionMark',
            BeforeDisconnectMacroDelay=100,
            BeforeDisconnectMacroEnterAfterCommand=False,
            BeforeDisconnectMacros=["A", "B", "C", "D", "E", "F\nG\nH"],
            BellMode='Visual',
            CloseOnDisconnect=True,
            CursorBlink='On',
            CursorKeyMode='Normal',
            CursorType='Block',
            Description='SSH Shell Entry Description',
            DisableKeypadMode='false',
            DoubleClickDelimiters=';',
            EnableLogging=True,
            EnableTCPKeepalives=True,
            Encoding='ISO_8859_13',
            Expiration=TOMORROW,
            FontMode='Override',
            ForceNonDestructiveBackspace=True,
            FunctionKeysMode='Linux',
            Group='Group Entry',
            GssApiAuthentication=True,
            HomeEndKeyMode='Standard',
            Host='Host',
            HostPort=21,
            InternetProtocol='IPv6',
            ImplicitCRinLF=True,
            ImplicitLFinCR=True,
            KeypadMode='Disable',
            Keywords='Tag1 Tag2',
            LocalEcho='Auto',
            LogMode='AllPrintableOutput',
            LogOverwriteMode='Append',
            LogPath='LogPath',
            MaxScrollbackLines=1000,
            MouseClickMode='Windows',
            OverrideTerminalName='OverrideTerminalName',
            Passphrase='Passphrase',
            Password='Password',
            # PrivateKeyConnectionID='Private Vault - Private Key Entry',
            PrivateKeyData='PrivateKeyData',
            PrivateKeyType='Data',
            PrivateKeyPassphrase='PKPassphrase',
            ProxyDnsLookupType='No',
            ProxyExcludedHosts='ProxyExcludedHost',
            ProxyHost='ProxyHost',
            ProxyHostPort='55',
            ProxyLocalHostConnections=True,
            ProxyMode='Custom',
            ProxyTelnetCommand='ProxyTelnetCommand',
            ProxyType='Socks5',
            ProxyUserName='ProxyUserName',
            ProxyPassword='ProxyPassword',
            RemoteCommand='RemoteCmd',
            ShowLogs=True,  # For displaying error messages
            SilentMode=False,
            SSHGatewayCredentialConnectionID=cred_entry_id,
            SSHGatewayCredentialSource='CredentialRepository',
            SSHGatewayHost='SSHGatewayHost',
            SSHGatewayPassword='SSHGWPassword',
            SSHGatewayPort='44',
            SSHGatewayPrivateKeyConnectionID=private_vault_key_id,
            SSHGatewayPrivateKeyPassphrase='SSHGWPKPassphrase',
            SSHGatewayPrivateKeyPromptForPassPhrase=False,
            SSHGatewayPrivateKeyType='PrivateVault',
            SSHGatewayUsername='SSHGW_Username',
            TCPKeepaliveInterval=2,
            TryAgent=True,
            UserName='Username',
            UseSSHGateway=True,
            UseX11Forwarding=True,
            Verbose=True,
            X11AuthorityFilePath='X11AuthorityFilePath',
            X11DisplayLocation='X11DisplayLocation',
            X11Protocol='XDMAuthorization1',
            Noshell=False)

TestLogger.info(" ")
TestLogger.info("           # Private vault entries #")
TestLogger.info("           ----------------------------------------")

DVLSTest.create_private_vault_entry_test(
            "Command Line Entry - Private",
            ConnectionType.CommandLine,
            CaptureOutputMode=CommandLineCaptureOutputMode.File.value,
            CaptureOutputFilePath='CapOutFilePath',
            CommandLine='CommandLineRun',
            CommandLineWaitForApplicationToExit=True,
            CredentialSource='Custom',
            CredentialConnectionId='CredConId',
            CredentialConnectionID='CredConID',
            Description='Description',
            Domain='Domain',
            EmbeddedWaitTime=500,
            ExecutionMode=CommandLineExecutionMode.Capture.value,
            Expiration=str(datetime.datetime.now()
                          + datetime.timedelta(1)),
            Group='Group Entry',
            Host='Host',
            Keywords='Tag1 Tag2',
            NetOnly=True,
            Parameter1DataType='Secured',
            Parameter1DefaultValue='P1Default',
            Parameter1Label='P1Label',
            Password='Password',
            ProcessName='CommandLineRun',
            Run64BitsMode=True,
            RunAsAdministrator=True,
            RunAsDomain='Domain',
            RunAsPassword='Password',
            RunAsPromptForCredentials=True,
            RunAsUsername='Username',
            UserName='Username')

private_vault_entry_id = ''
private_vault_entries_result = DVLS.get_private_vault_entries_by_name("Command Line Entry - Private", NO_DISPLAY)
if private_vault_entries_result.success:
    private_vault_entry_id = private_vault_entries_result.data[0]['id']

DVLSTest.modify_private_vault_entry_test(
            ConnectionType.CommandLine,
            private_vault_entry_id,
            CaptureOutputFilePath='CapOutFilePathB',
            CommandLine='CommandLineRunB',
            CommandLineWaitForApplicationToExit=False,
            Description='DescriptionB',
            Domain='DomainB',
            EmbeddedWaitTime=1000,
            Host='HostB',
            ProcessName='CommandLineRun',
            Run64BitsMode=False,
            UserName='UsernameB')

private_group_entry_id = ''
private_group_result = DVLS.get_private_vault_entries_by_name("Group Entry", NO_DISPLAY)
if private_group_result.success:
    private_group_entry_id = private_group_result.data[0]['id']

DVLSTest.get_private_vault_list_test(4)

DVLSTest.delete_private_vault_entry_test(private_vault_entry_id)

DVLSTest.delete_private_vault_entry_test(private_group_entry_id)

TestLogger.info(" ")
TestLogger.info("           # Modify entries on Default repository #")
TestLogger.info("           ----------------------------------------")

DVLSTest.modify_credential_test("Default", "Credential Entry", DEFAULT_REPO_ID,
                                UserName='UserName_B',
                                Password='Password_B',
                                Domain='Domain_B',
                                MnemonicPassword='MnemonicPassword_B')

RDP_Connected_Entries_result = DVLS.get_connections_by_name("RDP Configured Entry", DEFAULT_REPO_ID, NO_DISPLAY)
RDP_Connected_id = ''
if RDP_Connected_Entries_result.success:
    RDP_Connected_id = RDP_Connected_Entries_result.data[0].get('id')

DVLSTest.modify_connection_test("RDPConfigured",
                                RDP_Connected_id,
                               AdminMode=False,
                               AfterLoginDelay=2000,
                               AfterLoginExecuteProgram=False,
                               AfterLoginProgram='AftLoginPgm_B',
                               AllowBackgroundInput=False,
                               AllowOffline='false',
                               AlternateFullAddress='AltFullAdress_B',
                               AlternateShell='AltShell_B',
                               Animations=False,
                               AudioCaptureRedirectionMode=False,
                               AutoReconnection=True,
                               BandWidthAutoDetect=True,
                               BarPinned=True,
                               Centered=True,
                               Compression=True,
                               CustomHeight=2,
                               CustomWidth=2,
                               Description='RDP Configured Description B',
                               DesktopBackground=True,
                               DesktopComposition=False,
                               DisplayConnectionBar=True,
                               Domain='Domain_B',
                               EnableCredSSPSupport='false',
                               EnableSuperPan=False,
                               FontSmoothing=False,
                               GatewayHostname='GWHostname_B',
                               Group='Group Entry\Group Entry 2',
                               Host='Host_B',
                               KeepAliveInterval=22,
                               LoadAddOnsMode='false',
                               MinInputSendInterval=222,
                               NetworkAutoDetect=False,
                               NetworkLevelAuthentication=False,
                               MinimumLengthCount=2,  # For Password Validation
                               MinimumLowerCaseCount=2,  # For Password Validation
                               MinimumNumericCount=2,  # For Password Validation
                               MinimumSymbolCount=2,  # For Password Validation
                               MinimumUpperCaseCount=2,  # For Password Validation
                               MultiMonitors=False,
                               Password='PasswordB',
                               PasswordTemplateId=password_template_id,
                               # Default = '', Other possible values = 'Inherited', 'None', and 'NameOfTemplate'
                               PersistentBitmapCaching=True,
                               PingForGateway=False,
                               Port=2,
                               PromptCredentials=False,
                               PublicMode=False,
                               RDPLogOffWhenDisconnecting='false',
                               RedirectDirectX=False,
                               RestrictedAdminMode=False,
                               RemoteApp=False,
                               RemoteApplicationCmdLine='RemAppCmdLine_B',
                               RemoteApplicationProgram='RemAppPgm_B',
                               RequireCheckOutMode='true',
                               # RoleOverride='Everyone', #'Default', 'Everyone' or 'Never'
                               SecurityGroup=DVLS_SEC_GROUPS[1],
                               ShellWorkingDirectory='ShellWrkDir_B',
                               ShowContentWhileDragging=True,
                               SortPriority=2,
                               Span=False,
                               TimeBasedUsageDays="Mon-Tue-Wed-Thu-Fri",
                               # 'WeekEnds', 'Inherited'
                               # TimeBasedUsageHours='Inherited',
                               TimeBasedUsageTimePeriod=TIME_CURRENT + '-'
                                                        + TIME_IN_ONE_HOUR,
                               UseAlternateShell=False,
                               UserName='Username_B',
                               UsesClipboard=True,
                               UsesDevices=False,
                               UsesHardDrives=True,
                               UsesPrinters=False,
                               UseRedirectionServerName=False,
                               UsesSerialPorts=True,
                               UsesSmartDevices=False,
                               VisualStyles=True,
                               WinPostStr='WinPostStr_B',
                               WorkspaceId='WKSPCID_B')

DVLSTest.modify_password_template_test(password_template_id,
                                       Name="Password Configuration Entry 2",
                                       BracketsMin=5,
                                       CustomCharacters="@#$%&!",
                                       CustomCharactersMin=6,
                                       CustomExcludeCharacters="^¨`~°",
                                       DigitsMin=7,
                                       HighAnsiMin=8,
                                       Length=200,
                                       LowerCaseMin=9,
                                       MinusMin=10,
                                       PreviewPasswordCount=11,
                                       SpaceMin=12,
                                       SpecialCharMin=13,
                                       UnderlineMin=14,
                                       UpperCaseMin=15,
                                       XmlCompliant=True)

TestLogger.info(" ")
TestLogger.info("           # Sensitive data #")
TestLogger.info("           ----------------------------------------")
DVLSTest.get_sensitive_data_test(RDP_Connected_id,
                                 {'credentialConnectionId': '',
                                  'credentials': {'domain': 'Domain_B', 'password': 'PasswordB',
                                                  'userName': 'Username_B'},
                                  'gatewayCredentialConnectionID': cred_entry_id,
                                  'passwordItem': {'hasSensitiveData': True, 'sensitiveData': 'PasswordB'},
                                  'redirectedDrives': []})

DVLSTest.get_password_test(RDP_Connected_id, "PasswordB")

TestLogger.info(" ")
TestLogger.info("           # Delete connection by id #")
TestLogger.info("           ----------------------------------------")

DVLSTest.delete_connection_by_id_test(RDP_Connected_id)

TestLogger.info(" ")
TestLogger.info("           # Delete credential entry #")
TestLogger.info("           ----------------------------------------")
DVLSTest.delete_credential_by_id_test(cred_entry_id)


TestLogger.info(" ")
TestLogger.info("           # Modify Security Groups: #")
TestLogger.info("           ----------------------------------------")
for group in DVLS_SEC_GROUPS:
    newName = group + 'b'
    newDesc = newName + ' description'

    DVLSTest.modify_security_group_test(group,
                                        Name=newName,
                                        Description=newDesc)

TestLogger.info(" ")
TestLogger.info("           # Get Security Group Tree #")
TestLogger.info("           ----------------------------------------")
DVLSTest.get_security_group_tree_test(2)

TestLogger.info(" ")
TestLogger.info("           # Modify created roles #")
TestLogger.info("           ----------------------------------------")
for role_index,role in enumerate(DVLS_NEW_ROLES):
    newRoleName = role + 'b'
    newRoleDesc = newRoleName + ' description'
    if role_index == 0:
        DVLSTest.modify_role_by_name_test(role,
                                          Name=newRoleName,
                                          Description=newRoleDesc,
                                          IsAdministrator=True)
    else:
        DVLSTest.modify_role_by_id_test(role_RH_id,
                                        Name=newRoleName,
                                        Description=newRoleDesc,
                                        IsAdministrator=True)

TestLogger.info(" ")
TestLogger.info("           # Modify custom users #")
TestLogger.info("           ----------------------------------------")
for user_index, user in enumerate(DVLS_NEW_CUSTOM_USERS):
    if not user_index == len(DVLS_NEW_CUSTOM_USERS) - 1:
        eMail = 'mod' + ''.join(random.SystemRandom().choice(string.digits) for _ in range(5)) + '@dvls.com'
        DVLSTest.modify_user_by_name_test(user,
                                          IsAdmin=False,
                                          IsEnabled=True,
                                          ChangePW_NextLogon=False,
                                          Email=eMail,
                                          FirstName=user,
                                          LastName=user,
                                          CompanyName=user,
                                          JobTitle=user,
                                          Department=user,
                                          GravatarEmail=eMail,
                                          Address=user,
                                          State=user,
                                          CountryCode='CA',
                                          Phone=user,
                                          WorkPhone=user,
                                          CellPhone=user,
                                          Fax=user,
                                          Access=['RDM', 'DWL'],
                                          CustomRoles=[role_SA_id],
                                          Groups=[sec_group0, sec_group1],
                                          Privileges=['revealPW',
                                       'dragDrop',
                                       'viewDetails',
                                       'viewInfos',
                                       'viewUsageLogs',
                                       'import',
                                       'export'],
                                          Settings=['ReadWrite'])

last_user_id = None
last_user_id_result = DVLS.get_user_id(DVLS_NEW_CUSTOM_USERS[len(DVLS_NEW_CUSTOM_USERS) - 1], NO_DISPLAY)
if last_user_id_result.success:
    last_user_id = last_user_id_result.data
    DVLSTest.modify_user_by_id_test(last_user_id,
                                    IsAdmin=False,
                                    IsEnabled=True,
                                    ChangePW_NextLogon=False,
                                    Email=eMail,
                                    FirstName=user,
                                    LastName=user,
                                    CompanyName=user,
                                    JobTitle=user,
                                    Department=user,
                                    GravatarEmail=eMail,
                                    Address=user,
                                    State=user,
                                    CountryCode='CA',
                                    Phone=user,
                                    WorkPhone=user,
                                    CellPhone=user,
                                    Fax=user,
                                    Access=['RDM', 'DWL'],
                                    CustomRoles=[role_SA_id],
                                    Groups=[sec_group0, sec_group1],
                                    Privileges=['revealPW',
                                    'dragDrop',
                                    'viewDetails',
                                    'viewInfos',
                                    'viewUsageLogs',
                                    'import',
                                    'export'],
                                    Settings=['ReadWrite'])

TestLogger.info(" ")
TestLogger.info("           # Delete user #")
TestLogger.info("           ----------------------------------------")


DVLSTest.delete_user_by_id_test(last_user_id)

TestLogger.info(" ")
TestLogger.info("           # Delete role #")
TestLogger.info("           ----------------------------------------")
DVLSTest.delete_role_by_id_test(role_SA_id)

####################
#  NEGATIVE TESTS  #
####################

# DVLS.dvlsLogger.info("### Negative tests ###")
# DVLS.dvlsLogger.info("Create a user using a wrong domain")
# if DVLS.login(DVLS_ADMIN_USER, DVLS_ADMIN_PW):
#     result = DVLS.create_user('Domain', DVLS_NON_EXISTING_DOMAIN_USER, None)
#     if result == 1:
#         DVLS.logout(DVLS_ADMIN_USER)
#         if DVLS.login(DVLS_NON_EXISTING_DOMAIN_USER, '123456', verbose=False):
#             DVLS.dvlsLogger.info("Test Failed: user logged in using a wrong domain")
#             DVLS.logout(DVLS_NON_EXISTING_DOMAIN_USER)
#         else:
#             DVLS.dvlsLogger.info("Test Passed: unable to log in a user created with a wrong domain")
#             DVLStest.tests_succeeded += 1
#         DVLS.login(DVLS_ADMIN_USER, DVLS_ADMIN_PW)
#         DVLS.delete_user(DVLS_NON_EXISTING_DOMAIN_USER)
#     elif result == 2:
#         DVLS.dvlsLogger.info("Incomplete code : IS RESULT CODE 2 = FAIL BECAUSE OF WRONG DOMAIN ?")
#         DVLStest.tests_succeeded += 1
#     elif result == 0:
#         DVLS.dvlsLogger.info("Test Incomplete: unable to create user" + str(result))
# DVLS.logout(DVLS_ADMIN_USER)

TestLogger.info(" ")
TestLogger.info("           # Delete password template #")
TestLogger.info("           ----------------------------------------")
DVLSTest.delete_password_template_by_id_test(password_template_id)

run_cleanup()

############
#  TOTALS  #
############

TestLogger.info("\n\n### TOTALS ###")
TestLogger.info("Total tests passed: " + str(DVLSTest.tests_succeeded) + "/" + str(DVLSTest.total_tests) + "\n")
TestLogger.info("----------------------------------------------------------------------------------------------")
