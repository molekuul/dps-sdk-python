from dvlssdk.generated.enums.ConnectionLogMessage import *


class LogEntryEntity:
    def __init__(self):
        self.ActiveTime = None
        self.ActivityDuration = None
        self.Application = ''
        self.AssetElementID = None
        self.CloseMode = None
        self.ClosePrompt = ''
        self.Comment = ''
        self.ConnectionID = None
        self.ConnectionName = ''
        self.ConnectionTypeName = ''
        self.ConnectionUserName = ''
        self.Cost = None
        self.CreationDate = None
        self.CustomerID = None
        self.Data = ''
        self.Details = ''
        self.DetailsID = None
        self.EndDateTime = None
        self.EndDateTimeUTC = None
        self.GroupName = ''
        self.HostName = ''
        self.ID = None
        self.IsEmbedded = None
        self.LoggedUserName = ''
        self.MachineName = ''
        self.Message = ''
        self.MessageType = ConnectionLogMessage(0)
        self.MessageTypeTranslated = ''
        self.OpenMode = None
        self.Prompt = ''
        self.RepositoryID = None
        self.RepositoryName = ''
        self.SecurityGoup = ''
        self.StartDateTime = None
        self.StartDateTimeUTC = None
        self.Status = ''
        self.SupportClose = None
        self.UserName = ''
        self.Version = ''

