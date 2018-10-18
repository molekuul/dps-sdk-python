from dvlssdk.generated.enums.TimeBasedConnectionUsageDays import *
from dvlssdk.generated.enums.TimeBasedConnectionUsageHours import *


class TimeBasedUsageSettings:
    def __init__(self):
        self.SelectedDayOfWeek = 0
        self.TimeBasedUsageDays = TimeBasedConnectionUsageDays(0)
        self.TimeBasedUsageEndTime = ''
        self.TimeBasedUsageHours = TimeBasedConnectionUsageHours(0)
        self.TimeBasedUsageStartTime = ''

