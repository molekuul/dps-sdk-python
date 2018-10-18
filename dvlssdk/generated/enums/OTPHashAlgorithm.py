from enum import Enum


class OTPHashAlgorithm(Enum):
    SHA1 = 0
    SHA256 = 1
    SHA512 = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in OTPHashAlgorithm.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in OTPHashAlgorithm]
        return int_value in values
