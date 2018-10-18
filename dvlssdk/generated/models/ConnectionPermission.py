from dvlssdk.generated.enums.SecurityRoleOverride import *
from dvlssdk.generated.enums.SecurityRoleRight import *


class ConnectionPermission:
    def __init__(self):
        self.Override = SecurityRoleOverride(0)
        self.Right = SecurityRoleRight(0)
        self.Roles = []

