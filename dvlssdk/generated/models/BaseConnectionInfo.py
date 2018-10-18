from dvlssdk.generated.enums.ConnectionType import *


class BaseConnectionInfo:
    def __init__(self):
        self.ConnectionType = ConnectionType(0)
        self.Expiration = None
        self.Group = ''
        self.ID = ''
        self.ImageName = ''
        self.MasterSubType = ''
        self.Name = ''
        self.Repository = '00000000-0000-0000-0000-000000000000'
        self.SubType = ''

