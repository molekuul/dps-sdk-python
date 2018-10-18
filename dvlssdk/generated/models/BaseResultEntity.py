from dvlssdk.generated.enums.SaveResult import *


class BaseResultEntity:
    def __init__(self):
        self.DetailedErrorID = None
        self.DetailedErrorMessage = ''
        self.ErrorMessage = ''
        self.Exists = None
        self.IsWarning = False
        self.Result = SaveResult(0)

