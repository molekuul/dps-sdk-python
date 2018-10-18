from enum import Enum


class SyslogSenderProtocol(Enum):
    TCP = 0
    UDP = 1

    @staticmethod
    def value_from_name(typename):
        for name, member in SyslogSenderProtocol.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in SyslogSenderProtocol]
        return int_value in values
