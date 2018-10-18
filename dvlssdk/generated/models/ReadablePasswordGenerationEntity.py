from dvlssdk.generated.models.PasswordGenerationEntity import *


class ReadablePasswordGenerationEntity(PasswordGenerationEntity):
    def __init__(self):
        super().__init__()
        self.NumNumerics = 1
        self.NumSyllables = 1
        self.NumSymbols = 1

