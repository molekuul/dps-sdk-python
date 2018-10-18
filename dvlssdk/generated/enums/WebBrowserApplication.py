from enum import Enum


class WebBrowserApplication(Enum):
    Default = 0
    IE = 1
    FireFox = 2
    GoogleChrome = 3
    Safari = 4
    Opera = 5
    Edge = 6

    @staticmethod
    def value_from_name(typename):
        for name, member in WebBrowserApplication.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WebBrowserApplication]
        return int_value in values
