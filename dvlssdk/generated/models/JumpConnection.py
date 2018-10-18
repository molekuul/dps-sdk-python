from dvlssdk.generated.models.BaseConnection import *
from dvlssdk.generated.enums.JumpType import *


class JumpConnection(BaseConnection):
    def __init__(self):
        super().__init__()
        self.ConnectionID = None
        self.FilterIsJumpHost = True
        self.JumpType = JumpType(0)

