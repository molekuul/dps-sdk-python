from enum import Enum


class ApplicationSource(Enum):
    Default = 0
    RDM = 1
    PVM = 2
    Web = 3
    Agent = 4
    ChromeRDMExtension = 5
    FireFoxRDMExtension = 6
    IERDMExtension = 7
    SafariRDMExtension = 8
    ChromePVMExtension = 9
    FireFoxPVMExtension = 10
    IEPVMExtension = 11
    SafariPVMExtension = 12
    DVLSConsole = 13
    WebLogin = 14
    Scripting = 15
    Powershell = 16

    @staticmethod
    def value_from_name(typename):
        for name, member in ApplicationSource.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in ApplicationSource]
        return int_value in values
