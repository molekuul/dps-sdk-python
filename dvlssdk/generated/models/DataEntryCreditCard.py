from dvlssdk.generated.models.SensitiveItem import *


class DataEntryCreditCard:
    def __init__(self):
        self.CreditCardCustomerServicePhone = ''
        self.CreditCardExpirationMonth = SensitiveItem()
        self.CreditCardExpirationYear = SensitiveItem()
        self.CreditCardHideSensitive = False
        self.CreditCardInternationalServicePhone = ''
        self.CreditCardIssuingBank = ''
        self.CreditCardNumber = SensitiveItem()
        self.CreditCardOwner = ''
        self.CreditCardPassword = SensitiveItem()
        self.CreditCardPin = SensitiveItem()
        self.CreditCardSecureCode = SensitiveItem()
        self.CreditCardSecurity = SensitiveItem()
        self.CreditCardType = ''
        self.CreditCardValidFromMonth = SensitiveItem()
        self.CreditCardValidFromYear = SensitiveItem()
        self.CreditCardVerifiedBy = SensitiveItem()
        self.Url = ''

