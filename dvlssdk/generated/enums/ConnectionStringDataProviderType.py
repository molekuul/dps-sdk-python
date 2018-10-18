from enum import Enum


class ConnectionStringDataProviderType(Enum):
    SqlDataProvider = 0
    OracleDataProvider = 1
    OleDBDataProvider = 2
    OdbcDataProvider = 3
    SqlCeDataProvider = 4

    @staticmethod
    def value_from_name(typename):
        for name, member in ConnectionStringDataProviderType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ConnectionStringDataProviderType]
        return int_value in values
