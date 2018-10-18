from enum import Enum


class TelnetTerminalDnsLookupType(Enum):
    Automatic = 0
    Yes = 1
    No = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in TelnetTerminalDnsLookupType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TelnetTerminalDnsLookupType]
        return int_value in values
