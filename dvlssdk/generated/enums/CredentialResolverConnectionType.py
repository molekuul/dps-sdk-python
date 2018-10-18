from enum import Enum


class CredentialResolverConnectionType(Enum):
    Default = 0
    KeePass = 1
    LastPass = 2
    PasswordSafe = 3
    OnePassword = 4
    RoboForm = 5
    ChromePasswordManager = 6
    FirefoxPasswordManager = 7
    WindowsVault = 8
    PasswordVaultManager = 9
    AddOn = 10
    SecretServer = 11
    DataVault = 12
    ConnectionString = 13
    PrivateKey = 14
    Passwordstate = 15
    PleasantPasswordServer = 16
    AuthAnvilPasswordServer = 17
    ManagedEngine = 18
    AppleKeychain = 19
    CyberArk = 20
    PMPro = 21
    DVLS = 22
    PasswordBox = 23
    PassPortal = 24
    OTP = 25
    OneTimeCodeList = 26
    Custom = 27
    LAPS = 28
    Dashlane = 29
    TeamPass = 30
    TrueKey = 31
    StickyPassword = 32
    Hub = 33
    OnePasswordTeam = 34
    ZohoPassword = 35
    BeyondTrustPasswordSafe = 36
    SecurityPattern = 37
    CyberArkAim = 38
    PasswordList = 39
    TPAM = 40
    AzureVault = 41
    Bitwarden = 42

    @staticmethod
    def value_from_name(typename):
        for name, member in CredentialResolverConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in CredentialResolverConnectionType]
        return int_value in values
