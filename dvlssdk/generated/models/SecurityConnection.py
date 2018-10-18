from dvlssdk.generated.enums.AllowOffline import *
from dvlssdk.generated.models.BaseConnection import *
from dvlssdk.generated.enums.CheckOutMode import *
from dvlssdk.generated.enums.CredentialInheritedMode import *
from dvlssdk.generated.enums.PasswordComplexityUsage import *
from dvlssdk.generated.enums.PasswordComplexityValidation import *
from dvlssdk.generated.enums.RequireCheckOutMode import *
from dvlssdk.generated.enums.SecurityRoleOverride import *
from dvlssdk.generated.enums.TimeBasedConnectionUsageDays import *
from dvlssdk.generated.enums.TimeBasedConnectionUsageHours import *


class SecurityConnection(BaseConnection):
    def __init__(self):
        super().__init__()
        self.AllowOffline = AllowOffline(0)
        self.CheckOutMode = CheckOutMode(0)
        self.ComplexityInheritedMode = CredentialInheritedMode(0)
        self.PasswordComplexityCustomMinimumLength = 0
        self.PasswordComplexityCustomMinimumLowerCase = 0
        self.PasswordComplexityCustomMinimumNumeric = 0
        self.PasswordComplexityCustomMinimumSymbol = 0
        self.PasswordComplexityCustomMinimumUpperCase = 0
        self.PasswordComplexityId = ''
        self.PasswordComplexityUsageInheritedMode = CredentialInheritedMode(0)
        self.PasswordComplexityUsageOverride = PasswordComplexityUsage(0)
        self.PasswordComplexityValidationOverride = PasswordComplexityValidation(0)
        self.Permissions = []
        self.RequireCheckOutMode = RequireCheckOutMode(0)
        self.RoleOverride = SecurityRoleOverride(0)
        self.SelectedDayOfWeek = 0
        self.TimeBasedUsageDays = TimeBasedConnectionUsageDays(0)
        self.TimeBasedUsageEndTime = ''
        self.TimeBasedUsageHours = TimeBasedConnectionUsageHours(0)
        self.TimeBasedUsageStartTime = ''
        self.ViewOverride = SecurityRoleOverride(0)
        self.ViewRoles = []

