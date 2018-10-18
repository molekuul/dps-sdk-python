from dvlssdk.generated.models.AnalyzeRdmFileParameters import *
from dvlssdk.generated.models.ImportParameter import *


class ImportRdmFileParameters(AnalyzeRdmFileParameters):
    def __init__(self):
        super().__init__()
        self.DetailedParameters = []
        self.GlobalParameters = ImportParameter()

