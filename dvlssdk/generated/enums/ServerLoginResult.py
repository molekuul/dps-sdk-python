from enum import Enum


class ServerLoginResult(Enum):
    Error = 0
    Success = 1
    InvalidUserNamePassword = 2
    InvalidDataSource = 3
    DisabledDataSource = 4
    InvalidSubscription = 5
    TooManyUserForTheLicense = 6
    ExpiredSubscription = 7
    InGracePeriod = 8
    DisabledUser = 9
    UserNotFound = 10
    LockedUser = 11
    NotApprovedUser = 12
    BlackListed = 13
    InvalidIP = 14
    UnableToCreateUser = 15
    TwoFactorTypeNotConfigured = 16
    TwoFactorTypeActivatedNotAllowedClientSide = 17
    DomainNotTrusted = 18
    UserDoesNotBelongToDefaultDomain = 19
    InvalidGeoIP = 20
    TwoFactorIsRequired = 21
    TwoFactorPreconfigured = 22
    TwoFactorSecondStepIsRequired = 23
    TwoFactorUserIsDenied = 24
    TwoFactorSmsSended = 25
    TwoFactorTimeout = 26
    TwoFactorUserLockedOut = 27
    TwoFactorUserFraud = 28
    TwoFactorUserEmailNotConfigured = 29
    TwoFactorUserSmsNotConfigured = 30
    NotInTrustedGroup = 31
    ServerNotResponding = 32
    NotAccessToApplication = 33
    DirectoryNotResponding = 34
    WindowsAuthenticationFailure = 35
    ForcePasswordChange = 36

    @staticmethod
    def value_from_name(typename):
        for name, member in ServerLoginResult.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ServerLoginResult]
        return int_value in values
