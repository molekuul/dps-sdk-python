from dvlssdk.generated.models.BaseConnectionInfo import *


class ImportAnalyzeResult:
    def __init__(self):
        self.BaseConnectionInfo = BaseConnectionInfo()
        self.CanAdd = False
        self.CanEdit = False
        self.IsDuplicate = False
        self.Valid = False
        self.ValidationErrors = []

