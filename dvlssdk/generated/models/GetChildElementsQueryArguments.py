from dvlssdk.generated.enums.AssetElementSearchTarget import *
from dvlssdk.generated.models.QueryArguments import *


class GetChildElementsQueryArguments(QueryArguments):
    def __init__(self):
        super().__init__()
        self.EntryDefinitionKeys = []
        self.Target = AssetElementSearchTarget(0)

