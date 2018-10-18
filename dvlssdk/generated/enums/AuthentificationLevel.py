from enum import Enum


class AuthentificationLevel(Enum):
    ConnectDontWarnMe = 0
    DontConnect = 1
    WarnMe = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in AuthentificationLevel.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in AuthentificationLevel]
        return int_value in values
