from dvlssdk.generated.enums.EventSubscriptionType import *
from dvlssdk.generated.enums.SaveMode import *


class SubscriptionEntity:
    def __init__(self):
        self.EventSubscriptionType = EventSubscriptionType(0)
        self.GroupNames = None
        self.SaveMode = SaveMode(0)
        self.Filter = ''
        self.FilterID = None
        self.ID = None
        self.IsActive = False
        self.IsAdd = False
        self.IsDelete = False
        self.IsEdit = False
        self.UserID = None

