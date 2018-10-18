from enum import Enum


class ConnectionStringDataSourceType(Enum):
    SqlDataSource = 0
    SqlFileDataSource = 1
    OracleDataSource = 2
    AccessDataSource = 3
    OdbcDataSource = 4
    SqlCeDataSource = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in ConnectionStringDataSourceType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ConnectionStringDataSourceType]
        return int_value in values
