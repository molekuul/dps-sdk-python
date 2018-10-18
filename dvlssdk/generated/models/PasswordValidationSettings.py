from dvlssdk.generated.models.PasswordComplexity import *
from dvlssdk.generated.enums.PasswordComplexityUsage import *


class PasswordValidationSettings:
    def __init__(self):
        self.GroupMain = ''
        self.IsPrivateEntry = False
        self.Password = ''
        self.PasswordComplexity = PasswordComplexity()
        self.PasswordComplexityUsage = PasswordComplexityUsage(0)
        self.PasswordTemplateID = ''

