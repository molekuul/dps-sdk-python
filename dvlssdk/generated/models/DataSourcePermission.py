from dvlssdk.generated.enums.SecurityRoleDataSourceRight import *
from dvlssdk.generated.enums.SecurityRoleOverride import *


class DataSourcePermission:
    def __init__(self):
        self.Override = SecurityRoleOverride(0)
        self.Right = SecurityRoleDataSourceRight(0)
        self.Roles = []

