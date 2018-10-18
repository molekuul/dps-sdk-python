from dvlssdk.generated.models.BaseResultEntity import *
from dvlssdk.generated.models.TransferEntryIdentifier import *


class TransferResultDetailsEntity:
    def __init__(self):
        self.Identifier = TransferEntryIdentifier()
        self.Result = BaseResultEntity()

