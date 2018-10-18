from dvlssdk.generated.models.QueryArguments import *


class AttachmentQueryArguments(QueryArguments):
    def __init__(self):
        super().__init__()
        self.Private = False
        self.UseSensitiveMode = False

