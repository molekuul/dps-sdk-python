from dvlssdk.generated.enums.ApplicationPlatform import *
from dvlssdk.generated.enums.ApplicationSource import *
from dvlssdk.generated.enums.LoginAttemptFailType import *


class LoginHistoryModel:
    def __init__(self):
        self.CreationDate = None
        self.ExpirationDate = None
        self.LastUpdateDate = None
        self.Platform = ApplicationPlatform(0)
        self.SessionHash = ''
        self.Source = ApplicationSource(0)
        self.UserName = ''
        self.Ip = ''
        self.FailType = LoginAttemptFailType(0)

