from dvlssdk.generated.enums.ApplicationPlatform import *
from dvlssdk.generated.enums.ApplicationSource import *


class ClientApplicationInfo:
    def __init__(self):
        self.ApplicationPlatform = ApplicationPlatform(0)
        self.ApplicationSource = ApplicationSource(0)
        self.Version = ''

