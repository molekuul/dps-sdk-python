from enum import Enum


class SecurityRoleDataSourceRight(Enum):
    User = 0
    Role = 1
    Repository = 2
    SecurityGroup = 3
    DataSourceSettings = 4
    Export = 5
    Import = 6
    AddInRoot = 7
    Root = 8
    Report = 9
    ViewDeleted = 10
    ViewServerLogs = 11
    ViewLogs = 12
    Template = 13
    DefaultEntryTemplate = 14
    PasswordTemplate = 15
    ViewAdministrationLogs = 16
    RemoteTools = 17
    WebManagementTools = 18
    ConsoleManagementTools = 19
    MacroScriptTools = 20
    MacroScriptToolsEntry = 21

    @staticmethod
    def value_from_name(typename):
        for name, member in SecurityRoleDataSourceRight.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SecurityRoleDataSourceRight]
        return int_value in values
