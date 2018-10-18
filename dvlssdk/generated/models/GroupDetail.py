from dvlssdk.generated.enums.CredentialSourceMode import *
from dvlssdk.generated.enums.GroupConnectionType import *
from dvlssdk.generated.models.PartialConnectionCredentials import *
from dvlssdk.generated.models.SensitiveItem import *


class GroupDetail:
    def __init__(self):
        self.AllowAddEntryInGroup = True
        self.ConnectionString = ''
        self.ConsoleHost = ''
        self.ConsolePasswordItem = SensitiveItem()
        self.ConsoleUserName = ''
        self.CredentialConnectionId = ''
        self.CredentialMode = CredentialSourceMode(0)
        self.Credentials = PartialConnectionCredentials()
        self.Domain = ''
        self.GroupType = GroupConnectionType(0)
        self.Host = ''
        self.IP = ''
        self.PasswordItem = SensitiveItem()
        self.PrivateVaultSearchString = ''
        self.ShowComputersOnDashboard = False
        self.ShowGroupsOnDashboard = False
        self.ShowUsersOnDashboard = False
        self.UserName = ''

