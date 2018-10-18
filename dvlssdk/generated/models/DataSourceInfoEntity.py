from dvlssdk.generated.enums.SubscriptionProductType import *


class DataSourceInfoEntity:
    def __init__(self):
        self.AllowAttachments = False
        self.AllowConnectionLogs = False
        self.AllowSharing = False
        self.AttachmentSize = 0
        self.ConnectionCount = 0
        self.CreationDate = None
        self.Description = ''
        self.ID = None
        self.IsDeleted = False
        self.IsEnabled = True
        self.IsTrial = False
        self.License = ''
        self.LicenseExpiration = None
        self.MaxAttachmentSize = 0
        self.MaxConnectionCount = 0
        self.MaxUserCount = 0
        self.Name = ''
        self.SubscriptionType = SubscriptionProductType(0)
        self.UserCount = 0

