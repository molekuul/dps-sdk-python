from enum import Enum


class SessionToolConnectionType(Enum):
    CommandLine = 0
    PSExec = 1
    PowerShell = 2
    WMI = 3
    VBScript = 4
    Template = 5
    DatabaseQuery = 6
    PowerShellLocal = 7
    Macro = 8
    JitBit = 9
    WASPPowerShell = 10
    AutoIT = 11
    AutoHotKey = 12
    AppleScript = 13
    SSHCommandLine = 14
    ResetPassword = 15
    RemoteDeploy = 16
    Report = 17

    @staticmethod
    def value_from_name(typename):
        for name, member in SessionToolConnectionType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SessionToolConnectionType]
        return int_value in values
