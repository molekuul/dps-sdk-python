from dvlssdk.generated.enums.PartialConnectionCredentialsStatus import *


class PartialConnectionCredentials:
    def __init__(self):
        self.Domain = ''
        self.Password = ''
        self.Status = PartialConnectionCredentialsStatus(0)
        self.UserName = ''

