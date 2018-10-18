from dvlssdk.generated.models.UserAccountEntity import *
from dvlssdk.generated.models.UserProfileEntity import *
from dvlssdk.generated.models.UserSecurityEntity import *


class UserEntity:
    def __init__(self):
        self.Groups = []
        self.RoleGroups = []
        self.Roles = []
        self.SendEmailInvite = False
        self.UserAccount = UserAccountEntity()
        self.UserProfile = UserProfileEntity()
        self.UserSecurity = UserSecurityEntity()

