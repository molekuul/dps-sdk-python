from dvlssdk.generated.models.PasswordComplexity import *
from dvlssdk.generated.enums.PasswordGeneratorMode import *
from dvlssdk.generated.enums.PronounceableCaseMode import *


class PasswordConfiguration:
    def __init__(self):
        self.BracketsMin = 0
        self.Complexity = PasswordComplexity()
        self.CustomCharacters = ''
        self.CustomCharactersMin = 0
        self.CustomExcludeCharacters = ''
        self.DigitsMin = 0
        self.ExcludeCharacters = ''
        self.ExcludeLookAlike = False
        self.HighAnsiMin = 0
        self.ID = ''
        self.IncludeBrackets = False
        self.IncludeDigits = True
        self.IncludeHighAnsi = False
        self.IncludeHyphenate = False
        self.IncludeLowerCase = True
        self.IncludeMinus = False
        self.IncludeSpace = False
        self.IncludeSpecialChar = False
        self.IncludeUnderline = False
        self.IncludeUpperCase = True
        self.IsShared = False
        self.Length = 8
        self.LowerCaseMin = 0
        self.MinusMin = 0
        self.Mode = PasswordGeneratorMode(0)
        self.MorePronounceable = False
        self.MRUPatternArray = []
        self.Name = ''
        self.NoRepeatingCharacters = False
        self.Numerics = 1
        self.Pattern = ''
        self.PatternShuffleCharacters = True
        self.PreviewPasswordCount = 30
        self.PronounceableCaseMode = PronounceableCaseMode(0)
        self.SpaceMin = 0
        self.SpecialCharMin = 0
        self.Syllables = 1
        self.Symbols = 1
        self.UnderlineMin = 0
        self.UpperCaseMin = 0
        self.XmlCompliant = False

