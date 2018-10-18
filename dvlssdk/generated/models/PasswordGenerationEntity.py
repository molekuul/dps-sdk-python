from dvlssdk.generated.enums.PasswordGeneratorMode import *


class PasswordGenerationEntity:
    def __init__(self):
        self.PreviewPasswordCount = 30
        self.PasswordGeneratorMode = PasswordGeneratorMode(0)

