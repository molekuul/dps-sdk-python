class BaseCustomSecurity:
    def __init__(self):
        self.AllowDragAndDrop = True
        self.AllowRevealPassword = False
        self.CanExport = True
        self.CanImport = True
        self.CanMove = True
        self.CanViewDetails = True
        self.CanViewGlobalLogs = True
        self.CanViewInformations = True
        self.CustomRoles = []
        self.DenyAdd = []
        self.DenyAddInRoot = False
        self.DenyDelete = []
        self.DenyEdit = []
        self.DenyReveal = []
        self.IntegratedSecurity = False
        self.SubDataSource = ''
        self.UserSettingsValue = ''

