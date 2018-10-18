from enum import Enum


class SaveResult(Enum):
    Error = 0
    Success = 1
    AccessDenied = 2
    InvalidData = 3
    AlreadyExists = 4
    MaximumReached = 5
    NotFound = 6
    LicenseExpired = 7
    Unknown = 8
    TwoFactorTypeNotConfigured = 9
    WebApiRedirectToLogin = 10
    DuplicateLoginEmail = 11

    @staticmethod
    def value_from_name(typename):
        for name, member in SaveResult.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SaveResult]
        return int_value in values
