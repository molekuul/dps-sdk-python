from enum import Enum


class DuoStatus(Enum):
    OK = 0
    InvalidOrMissingParameters = 1
    InvalidOrMissingParametersOrUsernameAlreadyExists = 2
    AuthorizationAndOrDateHeadersWereMissingOrInvalid = 3
    Error = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in DuoStatus.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DuoStatus]
        return int_value in values
