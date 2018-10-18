from dvlssdk.generated.enums.ConnectionStateType import *


class ConnectionStateInformation:
    def __init__(self):
        self.ConnectionID = None
        self.ExpirationDate = None
        self.MachineName = ''
        self.State = ConnectionStateType(0)
        self.UserID = None

