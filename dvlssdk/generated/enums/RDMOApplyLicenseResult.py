from enum import Enum


class RDMOApplyLicenseResult(Enum):
    InvalidLicense = 0
    Success = 1
    AlreadyUsed = 2
    Expired = 3
    Error = 4
    TrialNotValid = 5
    MaximumReached = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in RDMOApplyLicenseResult.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in RDMOApplyLicenseResult]
        return int_value in values
