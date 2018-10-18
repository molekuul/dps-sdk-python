from enum import Enum


class EventSubscriptionType(Enum):
    Connection = 0
    DataSourceSettings = 1
    Group = 2
    Todo = 3
    User = 4
    Role = 5
    UserLockedOut = 6
    ConnectionOpened = 7
    Repository = 8

    @staticmethod
    def value_from_name(typename):
        for name, member in EventSubscriptionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in EventSubscriptionType]
        return int_value in values
