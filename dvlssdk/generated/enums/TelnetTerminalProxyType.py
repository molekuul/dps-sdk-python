from enum import Enum


class TelnetTerminalProxyType(Enum):
    none = 0
    Socks4 = 1
    Socks5 = 2
    Http = 3
    Telnet = 4
    Local = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in TelnetTerminalProxyType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in TelnetTerminalProxyType]
        return int_value in values
