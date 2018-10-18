from dvlssdk.generated.models.SensitiveItem import *


class DataEntryBankInfo:
    def __init__(self):
        self.BankAccountAddress = ''
        self.BankAccountOwner = ''
        self.BankAccountType = ''
        self.BankBranch = ''
        self.BankContact = ''
        self.BankName = ''
        self.BankPhone = ''
        self.BankPin = SensitiveItem()
        self.BankRoutingNumber = ''
        self.BankSWIFT = ''
        self.Url = ''

