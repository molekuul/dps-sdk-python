from enum import Enum


class PDFViewerType(Enum):
    Default = 0
    AcrobatReader = 1
    PDFXViewer = 2
    PDFXViewerPro = 3
    EmbeddedFireFox = 4
    Native = 5

    @staticmethod
    def value_from_name(typename):
        for name, member in PDFViewerType.__members__.items():
            if name.lower() == typename.lower():
                return member.value
        return 0

    @staticmethod
    def valid_value(int_value):
        values = [item.value for item in PDFViewerType]
        return int_value in values
