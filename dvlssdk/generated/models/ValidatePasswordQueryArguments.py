from dvlssdk.generated.models.QueryArguments import *


class ValidatePasswordQueryArguments(QueryArguments):
    def __init__(self):
        super().__init__()
        self.ElementID = None
        self.Password = ''

