from dvlssdk.generated.enums.ConnectionLogMessage import *


class RDMOLogEntry:
    def __init__(self):
        self.ActivityDuration = None
        self.CloseMode = None
        self.ClosePrompt = ''
        self.Comment = ''
        self.ConnectionID = None
        self.ConnectionName = ''
        self.ConnectionTypeName = ''
        self.ConnectionUserName = ''
        self.Cost = None
        self.CustomerID = None
        self.Data = ''
        self.EndDateTime = None
        self.GroupName = ''
        self.HostName = ''
        self.ID = None
        self.IsEmbedded = None
        self.MachineName = ''
        self.Message = ''
        self.MessageType = ConnectionLogMessage(0)
        self.OpenMode = None
        self.Prompt = ''
        self.RepositoryID = None
        self.SecurityGoup = ''
        self.StartDateTime = None
        self.Status = ''
        self.SupportClose = None
        self.UserName = ''

