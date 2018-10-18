from dvlssdk.generated.enums.ConnectionStringDataProviderType import *
from dvlssdk.generated.enums.ConnectionStringDataSourceType import *
from dvlssdk.generated.models.SensitiveItem import *


class CredentialConnectionString:
    def __init__(self):
        self.ConnectionString = SensitiveItem()
        self.DataProviderType = ConnectionStringDataProviderType(0)
        self.DataSourceType = ConnectionStringDataSourceType(0)

