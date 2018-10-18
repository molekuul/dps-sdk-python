from enum import Enum


class WebBrowserSubApplication(Enum):
    Default = 0
    MozNETR19_8 = 1
    SkyboundGecko = 2

    @staticmethod
    def value_from_name(typename):
        for name, member in WebBrowserSubApplication.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in WebBrowserSubApplication]
        return int_value in values
