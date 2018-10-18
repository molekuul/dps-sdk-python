from dvlssdk.generated.enums.OTPCodeSize import *
from dvlssdk.generated.enums.OTPHashAlgorithm import *
from dvlssdk.generated.models.SensitiveItem import *


class CredentialOTP:
    def __init__(self):
        self.OTPCodeSize = OTPCodeSize(0)
        self.OTPHashAlgorithm = OTPHashAlgorithm(0)
        self.OTPKeyItem = SensitiveItem()
        self.OTPTimeStep = 30
        self.AllowClipboard = False
        self.AllowViewPasswordAction = False

