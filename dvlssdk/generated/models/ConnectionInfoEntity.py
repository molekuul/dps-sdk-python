from dvlssdk.generated.enums.ConnectionType import *
from dvlssdk.generated.enums.IntelligentCacheAction import *


class ConnectionInfoEntity:
    def __init__(self):
        self.CachedSecurityGroups = []
        self.AttachmentCount = 0
        self.AttachmentPrivateCount = 0
        self.ConnectionType = ConnectionType(0)
        self.ConnexionTypeIcon = ''
        self.ConnexionTypeString = ''
        self.Data = ''
        self.GroupMain = ''
        self.HandbookCount = 0
        self.ID = None
        self.IntelligentCacheAction = IntelligentCacheAction(0)
        self.InventoryReportCount = 0
        self.MetaData = None        # ConnectionMetaDataEntity
        self.MetaDataString = ''
        self.RepositoryID = None
        self.SecurityGroup = None
        self.TodoOpenCount = 0
        self.Version = ''

