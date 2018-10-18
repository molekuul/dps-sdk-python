from dvlssdk.generated.enums.DateFilter import *


class LogFilterEntity:
    def __init__(self):
        self.ClosePrompt = ''
        self.Comment = ''
        self.ConnectionId = None
        self.ConnectionName = ''
        self.EndDate = None
        self.EndDateUTC = None
        self.GroupName = ''
        self.LoggedUserName = ''
        self.LogID = None
        self.MachineName = ''
        self.Message = ''
        self.Prompt = ''
        self.RepositoryID = None
        self.StartDate = None
        self.StartDateUTC = None
        self.UserName = ''
        self.IsClosePromptChecked = False
        self.IsGroupChecked = False
        self.IsPromptChecked = False
        self.IsMachineNameChecked = False
        self.IsMessageChecked = False
        self.IsUserNameChecked = False
        self.DateFilter = DateFilter(0)

