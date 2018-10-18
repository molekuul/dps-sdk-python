from dvlssdk.generated.enums.ConnectionDisplayMode import *
from dvlssdk.generated.models.DocumentConnection import *


class AttachmentItem:
    def __init__(self):
        self.AssetElementID = None
        self.ConnectionID = None
        self.CreatedBy = ''
        self.CreationDateTime = None
        self.Description = ''
        self.DisplayMode = ConnectionDisplayMode(0)
        self.Document = DocumentConnection()
        self.Filename = ''
        self.GroupName = ''
        self.HistoryID = ''
        self.ID = None
        self.IsPrivate = False
        self.PrivateSubType = ''
        self.SafePassword = ''
        self.SecurityGroup = None
        self.Size = 0
        self.Title = ''

