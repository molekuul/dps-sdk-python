from dvlssdk.generated.enums.UserLicenseType import *


class RDMOUserLicense:
    def __init__(self):
        self.CreationDate = None
        self.Description = ''
        self.ID = None
        self.LicenseExpiration = None
        self.LicenseName = ''
        self.LicenseSerial = ''
        self.LicenseType = UserLicenseType(0)
        self.ProductName = ''
        self.ProductVersion = ''

