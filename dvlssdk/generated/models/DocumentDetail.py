from dvlssdk.generated.enums.DocumentConnectionType import *
from dvlssdk.generated.enums.DocumentDataMode import *


class DocumentDetail:
    def __init__(self):
        self.FileExist = True
        self.CreatedBy = ''
        self.CreationDate = ''
        self.DataMode = DocumentDataMode(0)
        self.DocumentSize = 0
        self.FileName = ''
        self.Type = DocumentConnectionType(0)
        self.UseWebDefaultCredentials = False

