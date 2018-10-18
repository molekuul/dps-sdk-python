from enum import Enum


class LoginAttemptFailType(Enum):
    Error = 0
    UserName = 1
    Password = 2
    UserNamePassword = 3
    Expired = 4
    Locked = 5
    Disabled = 6
    InvalidIP = 7
    InvalidDataSource = 8
    DisabledDataSource = 9
    InvalidSubscription = 10
    TooManyUserForTheLicense = 11
    NotApproved = 12
    BlackListed = 13
    Success = 14
    UnableToCreateUser = 15
    TwoFactorFailed = 16
    TwoFactorUserIsDenied = 17
    TwoFactorSecondStepIsRequired = 18
    TwoFactorTimeout = 19
    TwoFactorUserFraud = 20
    TwoFactorUserLockedOut = 21
    TwoFactorSmsSended = 22
    TwoFactorUserEmailNotConfigured = 23
    TwoFactorUserSmsNotConfigured = 24
    NotAccessToApplication = 25

    @staticmethod
    def value_from_name(typename):
        for name, member in LoginAttemptFailType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in LoginAttemptFailType]
        return int_value in values
