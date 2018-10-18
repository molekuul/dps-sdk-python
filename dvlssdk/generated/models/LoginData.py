from dvlssdk.generated.models.RDMOLoginParameters import *
from dvlssdk.generated.models.TwoFactorInfo import *


class LoginData:
    def __init__(self):
        self.RDMOLoginParameters = RDMOLoginParameters()
        self.TwoFactorInfo = TwoFactorInfo()
        self.UserName = ''

