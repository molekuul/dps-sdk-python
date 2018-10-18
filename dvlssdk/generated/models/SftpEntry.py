from dvlssdk.generated.models.FtpNativeEntry import *


class SftpEntry(FtpNativeEntry):
    def __init__(self):
        super().__init__()
        self.Port = 22
        self.ShowHiddenFiles = False

