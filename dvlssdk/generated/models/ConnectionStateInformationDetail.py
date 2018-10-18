from dvlssdk.generated.models.ConnectionStateInformation import *


class ConnectionStateInformationDetail(ConnectionStateInformation):
    def __init__(self):
        super().__init__()
        self.Comment = ''
        self.CreationDate = None
        self.CreationLoggedUserName = ''
        self.CreationUsername = ''
        self.RepositoryID = None

