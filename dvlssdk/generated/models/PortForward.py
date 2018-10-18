from dvlssdk.generated.enums.PortForwardMode import *


class PortForward:
    def __init__(self):
        self.Destination = ''
        self.DestinationPort = 0
        self.ID = ''
        self.Mode = PortForwardMode(0)
        self.Source = ''
        self.SourcePort = 0

