from dvlssdk.generated.enums.BrowserExtensionLinkerCompareType import *


class BrowserExtensionMetaData:
    def __init__(self):
        self.Enabled = False
        self.UseRegularExpression = False
        self.RegularExpression = ''
        self.CompareType = BrowserExtensionLinkerCompareType(0)

