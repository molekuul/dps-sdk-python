from dvlssdk.generated.models.PasswordGenerationEntity import *
from dvlssdk.generated.enums.PronounceableCaseMode import *


class PronounceablePasswordGenerationEntity(PasswordGenerationEntity):
    def __init__(self):
        super().__init__()
        self.CustomCharacters = ''
        self.IncludeDigits = True
        self.Length = 8
        self.MorePronounceable = False
        self.PronounceableCaseMode = PronounceableCaseMode(0)

