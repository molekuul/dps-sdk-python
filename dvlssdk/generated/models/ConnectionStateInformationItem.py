from dvlssdk.generated.models.ConnectionStateInformation import *


class ConnectionStateInformationItem(ConnectionStateInformation):
    def __init__(self):
        super().__init__()
        self.ConnectionName = ''
        self.Group = ''
        self.User = ''

