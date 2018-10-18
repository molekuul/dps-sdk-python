from enum import Enum


class RDPGatewayCredentialsSource(Enum):
    UserPassword = 0
    Smartcard = 1
    AskMeLater = 4
    GatewayAccessToken = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in RDPGatewayCredentialsSource.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDPGatewayCredentialsSource]
        return int_value in values
