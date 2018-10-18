from dvlssdk.generated.enums.ConnectionLogGridDateKind import *


class LogAdministrationFilter:
    def __init__(self):
        self.DateKind = ConnectionLogGridDateKind(0)
        self.EndDate = None
        self.EndDateUTC = None
        self.FilterName = ''
        self.LoggedUserName = ''
        self.MachineName = ''
        self.Message = ''
        self.StartDate = None
        self.StartDateUTC = None
        self.UserName = ''

