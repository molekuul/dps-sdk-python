from enum import Enum


class DateFilter(Enum):
    LastWeek = 0
    Today = 1
    Yesterday = 2
    Custom = 3
    LastMonth = 4
    CurrentMonth = 5
    Last7Days = 6
    Last30Days = 7
    Last31Days = 8
    Last60Days = 9
    Last90Days = 10

    @staticmethod
    def value_from_name(typename):
        for name, member in DateFilter.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in DateFilter]
        return int_value in values
