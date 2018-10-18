from enum import Enum


class TimeBasedConnectionUsageHours(Enum):
    Default = 0
    AnyTime = 1
    Datasource = 2
    Inherited = 3
    Custom = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in TimeBasedConnectionUsageHours.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TimeBasedConnectionUsageHours]
        return int_value in values
