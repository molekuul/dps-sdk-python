from enum import Enum


class DataEntryConnectionType(Enum):
    Default = 0
    Credential = 1
    CreditCard = 2
    Alarm = 3
    BankInfo = 4
    TravelInfo = 5
    Custom = 6
    AddOn = 7
    Serial = 8
    EmailAccount = 9
    SecureNote = 10
    Web = 11
    Passport = 12
    SafetyDeposit = 13
    Wallet = 14
    Wifi = 15
    ApplicationSendKey = 16
    DriverLicense = 17
    SocialSecurityNumber = 18
    Membership = 19
    DoorEntryCode = 20

    @staticmethod
    def value_from_name(typename):
        for name, member in DataEntryConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DataEntryConnectionType]
        return int_value in values
