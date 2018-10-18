from dvlssdk.generated.enums.DataEntryWalletType import *
from dvlssdk.generated.models.SensitiveItem import *


class DataEntryWallet:
    def __init__(self):
        self.Url = ''
        self.WalletDriverLicense = ''
        self.WalletMembership = ''
        self.WalletSocialSecurityNumberItem = SensitiveItem()
        self.WalletType = DataEntryWalletType(0)

