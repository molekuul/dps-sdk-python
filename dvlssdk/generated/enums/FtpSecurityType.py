from enum import Enum


class FtpSecurityType(Enum):
    NoSecurity = 0
    ExplicitTLSorSSL = 1
    ImplicitTLSorSSL = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in FtpSecurityType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in FtpSecurityType]
        return int_value in values
