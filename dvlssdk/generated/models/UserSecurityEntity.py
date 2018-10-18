from dvlssdk.generated.models.CustomSecurity import *
from dvlssdk.generated.enums.DefaultBoolean import *
from dvlssdk.generated.enums.UserLicenceTypeMode import *


class UserSecurityEntity:
    def __init__(self):
        self.CustomSecurityEntity = CustomSecurity()
        self.DeleteSQLLogin = DefaultBoolean(0)
        self.IsServerUserTypeAssumed = False
        self.RepositoryEntities = []
        self.AuthenticationType = None
        self.CanAdd = False
        self.CanDelete = False
        self.CanEdit = False
        self.CreatedByLoggedUserName = ''
        self.CreatedByUserName = ''
        self.CreationDate = None
        self.CustomSecurity = ''
        self.HasAccessPVM = True
        self.HasAccessRDM = True
        self.HasAccessWeb = True
        self.HasAccessWebLogin = True
        self.ID = None
        self.IsAdministrator = False
        self.IsEnabled = True
        self.IsLockedOut = False
        self.LastLockoutDate = None
        self.LoginEmail = ''
        self.ModifiedDate = None
        self.ModifiedLoggedUserName = ''
        self.ModifiedUserName = ''
        self.Name = ''
        self.Repositories = ''
        self.SecurityKey = ''
        self.UPN = ''
        self.UserLicenceType = UserLicenceTypeMode(0)
        self.UserType = 0

