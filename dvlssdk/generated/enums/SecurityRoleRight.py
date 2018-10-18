from enum import Enum


class SecurityRoleRight(Enum):
    View = 0
    ViewPassword = 1
    Add = 2
    Delete = 3
    Edit = 4
    EditStatus = 5
    EditDescription = 6
    EditSecurity = 7
    PasswordHistory = 8
    ConnectionHistory = 9
    RemoteTools = 10
    Attachment = 11
    EditAttachment = 12
    Inventory = 13
    ViewLogs = 14
    Handbook = 15
    EditHandbook = 16
    WebManagementTools = 17
    ConsoleManagementTools = 18
    MacroScriptTools = 19
    MacroScriptToolsEntry = 20
    EditPassword = 21

    @staticmethod
    def value_from_name(typename):
        for name, member in SecurityRoleRight.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SecurityRoleRight]
        return int_value in values
