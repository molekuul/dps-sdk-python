from dvlssdk.generated.enums.SecureNoteType import *
from dvlssdk.generated.models.SensitiveItem import *


class DataEntrySecureNote:
    def __init__(self):
        self.EncryptedSecureNote = ''
        self.SecureNoteIsProtected = False
        self.SecureNoteRtf = SensitiveItem()
        self.SecureNoteType = SecureNoteType(0)
        self.Url = ''

