from enum import Enum


class PronounceableCaseMode(Enum):
    LowerCase = 0
    UpperCase = 1
    MixedCase = 2
    RandomCase = 3
    RandomMixedCase = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in PronounceableCaseMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PronounceableCaseMode]
        return int_value in values
