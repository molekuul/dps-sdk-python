from enum import Enum


class PasswordQualityEstimator(Enum):
    none = 0
    PopularPassword = 1
    Forbidden = 2
    VeryWeak = 3
    Weak = 4
    Good = 5
    Strong = 6
    VeryStrong = 7
    Perfect = 8

    @staticmethod
    def value_from_name(typename):
        for name, member in PasswordQualityEstimator.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PasswordQualityEstimator]
        return int_value in values
