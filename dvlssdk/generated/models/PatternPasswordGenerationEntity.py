from dvlssdk.generated.models.PasswordGenerationEntity import *


class PatternPasswordGenerationEntity(PasswordGenerationEntity):
    def __init__(self):
        super().__init__()
        self.Pattern = ''
        self.PatternShuffleCharacters = True

