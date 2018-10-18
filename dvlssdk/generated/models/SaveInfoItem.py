from dvlssdk.generated.enums.SaveMode import *
from dvlssdk.generated.enums.SaveResult import *


class SaveInfoItem:
    def __init__(self):
        self.ID = None
        self.Result = SaveResult(0)
        self.SaveMode = SaveMode(0)

