from enum import Enum


class WebBrowserAuthenticationMode(Enum):
    Form = 0
    Basic = 1
    Digest = 2
    Ntlm = 3

    @staticmethod
    def value_from_name(typename):
        for name, member in WebBrowserAuthenticationMode.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WebBrowserAuthenticationMode]
        return int_value in values
