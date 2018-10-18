from dvlssdk.generated.models.BaseConnection import *
from dvlssdk.generated.enums.DocumentConnectionType import *
from dvlssdk.generated.enums.DocumentDataMode import *
from dvlssdk.generated.enums.PDFViewerType import *


class DocumentConnection(BaseConnection):
    def __init__(self):
        super().__init__()
        self.TextDocumentFormat = ''
        self.AllowExport = True
        self.AllowExportForEveryone = False
        self.AllowPreview = True
        self.ConnectionSubType = ''
        self.Data = ''
        self.DocumentDataMode = DocumentDataMode(0)
        self.DocumentType = DocumentConnectionType(0)
        self.EmbeddedData = ''
        self.EmbeddedDataID = ''
        self.Filename = ''
        self.Password = ''
        self.PDFViewer = PDFViewerType(0)
        self.Program = ''
        self.ReadOnly = True
        self.Run64BitsMode = False
        self.EditOnOpen = False
        self.Title = ''
        self.RunAsAdministrator = False
        self.SafePassword = ''
        self.Size = 0
        self.UseDefaultWorkingDirectory = True
        self.UseShellExecute = True
        self.UseWebDefaultCredentials = False
        self.WorkingDirectory = ''

