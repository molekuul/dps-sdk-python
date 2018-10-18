from dvlssdk.generated.enums.Gender import *
from dvlssdk.generated.models.SensitiveItem import *


class DataEntryPassport:
    def __init__(self):
        self.CountryCode = ''
        self.Expiration = None
        self.FirstName = ''
        self.Gender = Gender(0)
        self.LastName = ''
        self.MiddleName = ''
        self.NumberItem = SensitiveItem()
        self.Url = ''

