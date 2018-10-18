from enum import Enum


class EmailAuthenticationType(Enum):
    AppleToken = 0
    HTTPMD5Digest = 1
    MD5ChallengeResponse = 2
    NTLM = 3
    Password = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in EmailAuthenticationType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in EmailAuthenticationType]
        return int_value in values
