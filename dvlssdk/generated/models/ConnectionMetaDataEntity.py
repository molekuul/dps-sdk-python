from dvlssdk.generated.models.BrowserExtensionMetaData import *
from dvlssdk.generated.enums.ConnectionType import *
from dvlssdk.generated.models.SecurityConnection import *


class ConnectionMetaDataEntity:
    def __init__(self):
        self.BrowserExtensionMetaData = BrowserExtensionMetaData()
        self.ConnectionMasterSubType = ''
        self.ConnectionSubType = ''
        self.ConnectionType = ConnectionType(0)
        self.DataSourcePermissions = []
        self.Description = ''
        self.Expiration = None
        self.Group = ''
        self.GroupMain = ''
        self.Host = ''
        self.Image = None
        self.ImageName = ''
        self.Keywords = ''
        self.Name = ''
        self.Security = SecurityConnection()
        self.SharedTemplate = False
        self.SortPriority = 0
        self.Status = ''
        self.StatusMessage = ''
        self.Url = ''

