from dvlssdk.generated.enums.DVLSEdition import *


class SerialInformationsEntity:
    def __init__(self):
        self.Edition = DVLSEdition(0)
        self.Expiration = None
        self.IsValidSerial = False
        self.MaxUserCount = 0

