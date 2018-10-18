from dvlssdk.generated.enums.RepositoryType import *


class RepositoryEntity:
    def __init__(self):
        self.RepositoryType = RepositoryType(0)
        self.Selected = False
        self.CreationDate = None
        self.Description = ''
        self.ID = None
        self.ModifiedDate = None
        self.ModifiedLoggedUserName = ''
        self.ModifiedUserName = ''
        self.Name = ''

