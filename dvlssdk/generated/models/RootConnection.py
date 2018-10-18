from dvlssdk.generated.models.BaseConnection import *
from dvlssdk.generated.enums.HandbookTemplateType import *


class RootConnection(BaseConnection):
    def __init__(self):
        super().__init__()
        self.AllowClearPasswordHistory = True
        self.AllowDataEntryMultiSelect = False
        self.AllowInformationNote = False
        self.AllowRTF = False
        self.CustomProxyServerHost = ''
        self.CustomProxyServerPort = 8999
        self.DataVersion = 0
        self.Domain = ''
        self.HandbookDefaultCustomTemplateID = ''
        self.HandbookStyleSheets = []
        self.HandbookTemplates = []
        self.HandbookTemplateType = HandbookTemplateType(0)
        self.Password = ''
        self.Permissions = []
        self.SafePassword = ''
        self.TreeViewCustomField1ColumnLabel = ''
        self.TreeViewCustomField2ColumnLabel = ''
        self.TreeViewCustomField3ColumnLabel = ''
        self.UserName = ''

