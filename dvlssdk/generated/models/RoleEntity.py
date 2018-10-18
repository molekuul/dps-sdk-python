from dvlssdk.generated.models.UserEntity import *


class RoleEntity(UserEntity):
    def __init__(self):
        super().__init__()
        self.IsFromActiveDirectory = False

