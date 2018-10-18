from dvlssdk.generated.enums.PasswordComplexityValidation import *


class PasswordComplexity:
    def __init__(self):
        self.ID = ''
        self.MinimumLengthCount = 0
        self.MinimumLowerCaseCount = 0
        self.MinimumNumericCount = 0
        self.MinimumSymbolCount = 0
        self.MinimumUpperCaseCount = 0
        self.Name = ''
        self.Validation = PasswordComplexityValidation(0)

