from ...generated.enums.CheckOutMode import CheckOutMode
from ...generated.models.ConnectionStateInformationDetail import ConnectionStateInformationDetail
from ...generated.enums.ConnectionStatusBehavior import ConnectionStatusBehavior
from ...generated.enums.ConnectionType import ConnectionType
from ...custom.models.PartialConnectionPermissions import PartialConnectionPermissions
from ...generated.enums.PasswordComplexityUsage import PasswordComplexityUsage
from ...generated.enums.RequireCheckOutMode import RequireCheckOutMode
from ...generated.models.RootConnection import RootConnection
from ...generated.models.SecurityConnection import SecurityConnection
from ...generated.models.TimeBasedUsageSettings import TimeBasedUsageSettings


class PartialConnection:
    def __init__(self):
        self.AttachmentCount = 0
        self.CheckOutMode = CheckOutMode(0)
        self.ConnectionStateInformationDetail = ConnectionStateInformationDetail()
        self.ConnectionSubType = ''
        self.ConnectionType = ConnectionType(0)
        self.CreatedBy = ''
        self.CreatedDate = ''
        self.Data = None
        self.DatabaseId = ''
        self.Description = ''
        self.Domain = ''
        self.Expiration = None
        self.Group = ''
        self.GroupName = ''
        self.Id = None
        self.ImageBytes = ''
        self.ImageBytesUrl = ''
        self.ImageName = ''
        self.InventoryReportCount = 0
        self.IsExpired = False
        self.IsPrivate = False
        self.IsVirtual = False
        self.Keywords = ''
        self.LargeImageBytesUrl = ''
        self.MinimumLengthCount = 0
        self.MinimumLowerCaseCount = 0
        self.MinimumNumericCount = 0
        self.MinimumSymbolCount = 0
        self.MinimumUpperCaseCount = 0
        self.ModifiedBy = ''
        self.ModifiedDate = ''
        self.Name = ''
        self.OriginalName = ''
        self.PartialConnections = []
        self.Password = ''
        self.PasswordTemplateId = ''
        self.PasswordValidationUsage = PasswordComplexityUsage(0)
        self.Permissions = PartialConnectionPermissions()
        self.RequireCheckOutMode = RequireCheckOutMode(0)
        self.Root = RootConnection()
        self.Security = SecurityConnection()
        self.SecurityGroupId = ''
        self.SecurityGroupName = ''
        self.SortPriority = 0
        self.Status = ConnectionStatusBehavior(0)
        self.StatusLockedBy = ''
        self.StatusMessage = ''
        self.StatusMessages = []
        self.TimeBasedUsageSettings = TimeBasedUsageSettings()
        self.TypeDescription = ''
        self.TypeId = ''
        self.UserName = ''
        self.IsJumpHost = False
        self.TemplateName = ''
