from enum import Enum


class PromptForOfflinePassword(Enum):
    Never = 0
    AlwaysPrompt = 1
    PromptIfAskForPassword = 2
    PromptOnOpenOffline = 3
    PromptOnOpenOfflineIfAskForPassword = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in PromptForOfflinePassword.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PromptForOfflinePassword]
        return int_value in values
