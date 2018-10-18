from dvlssdk.generated.enums.CustomInstallerStatus import *


class RDMOCustomInstaller:
    def __init__(self):
        self.CreationDate = None
        self.Description = ''
        self.ErrorMessage = ''
        self.GenerationDate = None
        self.ID = ''
        self.Name = ''
        self.Status = CustomInstallerStatus(0)
        self.TemplateName = ''
        self.UserID = ''
        self.UserName = ''

