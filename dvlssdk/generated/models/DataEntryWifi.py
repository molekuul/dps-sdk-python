from dvlssdk.generated.models.SensitiveItem import *
from dvlssdk.generated.enums.WifiSecurity import *


class DataEntryWifi:
    def __init__(self):
        self.AirPortId = ''
        self.AttachedStoragePasswordItem = SensitiveItem()
        self.BaseStationName = ''
        self.BaseStationPasswordItem = SensitiveItem()
        self.NetworkName = ''
        self.ServerIpAddress = ''
        self.SupportPhoneNumber = ''
        self.Url = ''
        self.WirelessNetworkPasswordItem = SensitiveItem()
        self.WirelessSecurity = WifiSecurity(0)

