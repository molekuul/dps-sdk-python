from dvlssdk.generated.models.PasswordGenerationEntity import *


class SpecifiedPasswordGenerationEntity(PasswordGenerationEntity):
    def __init__(self):
        super().__init__()
        self.BracketsMin = 0
        self.CustomCharacters = ''
        self.CustomCharactersMin = 0
        self.CustomExcludeCharacters = ''
        self.DigitsMin = 0
        self.HighAnsiMin = 0
        self.IncludeBrackets = False
        self.IncludeDigits = True
        self.IncludeHighAnsi = False
        self.IncludeLowerCase = True
        self.IncludeMinus = False
        self.IncludeSpace = False
        self.IncludeSpecialChar = False
        self.IncludeUnderline = False
        self.IncludeUpperCase = True
        self.Length = 8
        self.LowerCaseMin = 0
        self.MinusMin = 0
        self.SpaceMin = 0
        self.SpecialCharMin = 0
        self.UnderlineMin = 0
        self.UpperCaseMin = 0
        self.XmlCompliant = False

