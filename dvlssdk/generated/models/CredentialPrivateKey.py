from dvlssdk.generated.enums.PrivateKeyType import *
from dvlssdk.generated.models.SensitiveItem import *


class CredentialPrivateKey:
    def __init__(self):
        self.AllowClipboard = False
        self.AllowViewPasswordAction = False
        self.PrivateKeyAutomaticallyLoadToKeyAgent = False
        self.PrivateKeyData = ''
        self.PrivateKeyFileName = ''
        self.PrivateKeyOverridePasswordItem = SensitiveItem()
        self.PrivateKeyOverrideUsername = ''
        self.PrivateKeyPassPhraseItem = SensitiveItem()
        self.PrivateKeyPromptForPassPhrase = False
        self.PrivateKeyType = PrivateKeyType(0)

