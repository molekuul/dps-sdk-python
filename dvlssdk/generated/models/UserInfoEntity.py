from dvlssdk.generated.models.CustomSecurity import *
from dvlssdk.generated.enums.ServerUserType import *


class UserInfoEntity:
    def __init__(self):
        self.AuthenticationType = None
        self.CanAdd = False
        self.CanDelete = False
        self.CanEdit = False
        self.ConnectionOverrides = ''
        self.ConnectionOverridesCacheID = ''
        self.CreationDate = None
        self.Email = ''
        self.FullName = ''
        self.HasAccessPVM = True
        self.HasAccessRDM = True
        self.HasAccessWeb = True
        self.HasAccessWebLogin = True
        self.ID = None
        self.IsAdministrator = False
        self.IsEnabled = True
        self.IsOwner = False
        self.IsTemplate = False
        self.LoginEmail = ''
        self.Name = ''
        self.PasswordFormat = 0
        self.Repositories = ''
        self.ResetTwoFactor = False
        self.SecurityKey = ''
        self.UPN = ''
        self.UserMustChangePasswordAtNextLogon = False
        self.CustomSecurity = ''
        self.CustomSecurityValue = CustomSecurity()
        self.GroupInfos = []
        self.IsChangePasswordAllowed = False
        self.IsGroupLoaded = False
        self.IsRoleLoaded = False
        self.RoleGroupInfos = []
        self.Roles = []
        self.SerializeCustomSecurityValue = False
        self.ServerUserType = ServerUserType(0)
        self.UserType = ServerUserType(0)

