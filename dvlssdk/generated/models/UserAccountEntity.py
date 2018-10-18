from dvlssdk.generated.models.TwoFactorInfo import *
from dvlssdk.generated.enums.UserEntityPasswordFormat import *


class UserAccountEntity:
    def __init__(self):
        self.HasPrivateVault = False
        self.IsChangePasswordAllowed = False
        self.Password = ''
        self.PasswordFormat = UserEntityPasswordFormat(0)
        self.TwoFactorInfo = TwoFactorInfo()
        self.ConnectionOverrides = ''
        self.ConnectionOverridesCacheID = ''
        self.CreatedByLoggedUserName = ''
        self.CreatedByUserName = ''
        self.CreationDate = None
        self.Data = ''
        self.Email = ''
        self.FullName = ''
        self.ID = None
        self.IsOwner = False
        self.IsTemplate = False
        self.LastLoginDate = None
        self.ModifiedDate = None
        self.ModifiedLoggedUserName = ''
        self.ModifiedUserName = ''
        self.ResetTwoFactor = False
        self.SecurityKey = ''
        self.UserMustChangePasswordAtNextLogon = False

