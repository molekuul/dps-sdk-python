from enum import Enum


class TlsOption(Enum):
    NotSpecified = 0
    none = 1
    Ssl = 2
    X509 = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in TlsOption.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TlsOption]
        return int_value in values
