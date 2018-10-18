from dvlssdk.generated.models.BaseCustomSecurity import *
from dvlssdk.generated.enums.OfflineMode import *
from dvlssdk.generated.enums.TlsOption import *


class CustomSecurity(BaseCustomSecurity):
    def __init__(self):
        super().__init__()
        self.AllowPersonalConnection = True
        self.OfflineMode = OfflineMode(0)
        self.TlsOption = TlsOption(0)

