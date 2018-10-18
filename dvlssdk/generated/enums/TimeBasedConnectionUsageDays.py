from enum import Enum


class TimeBasedConnectionUsageDays(Enum):
    Default = 0
    AnyDay = 1
    Datasource = 2
    Inherited = 3
    WeekDays = 4
    WeekEnds = 5
    Custom = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in TimeBasedConnectionUsageDays.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TimeBasedConnectionUsageDays]
        return int_value in values
