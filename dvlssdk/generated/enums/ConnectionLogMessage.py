from enum import Enum


class ConnectionLogMessage(Enum):
    Unknown = 0
    Info = 1
    Warning = 2
    Error = 3
    OpenConnection = 4
    AddConnection = 5
    EditConnection = 6
    DeleteConnection = 7
    OpenVPN = 8
    CloseVPN = 9
    CredentialsSentToPlugin = 10
    Comment = 11
    ExportedConnection = 12
    UserAdded = 13
    UserDeleted = 14
    UserEdited = 15
    SecurityGroupAdded = 16
    SecurityGroupDeleted = 17
    SecurityGroupEdited = 18
    RoleAdded = 19
    RoleDeleted = 20
    RoleEdited = 21
    MacroScriptTool = 22
    ExportedDocuments = 23
    KeyAgentKeyUsed = 24
    ReportOpened = 25
    RepositoryAdded = 26
    RepositoryDeleted = 27
    RepositoryEdited = 28
    AttachmentAdded = 29
    AttachmentDeleted = 30
    AttachmentEdited = 31
    AttachmentFileUploaded = 32
    AttachmentFileOpened = 33
    PasswordChanged = 44
    AttachmentOpened = 45
    PasswordHistoredCleared = 46
    ResetPassword = 53
    Checkout = 54
    Checkin = 55
    PermissionChanged = 56
    Validation = 57

    @staticmethod
    def value_from_name(typename):
        for name, member in ConnectionLogMessage.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ConnectionLogMessage]
        return int_value in values
