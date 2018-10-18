from dvlssdk.generated.enums.SaveResult import SaveResult
class SDKResult:

    def __init__(self, apiResult = {'result': 0, 'data': None}):
        if isinstance(apiResult, dict):
            if 'data' in apiResult:
                self.data = apiResult.get('data')
            else:
                self.data = {}

            self.result = apiResult.get('result')

            if apiResult.get('errorMessage'):
                self.errorMessage = apiResult.get('errorMessage')
            else:
                self.errorMessage = ''
        elif isinstance(apiResult, SDKResult):
            self.result = apiResult.result
            self.errorMessage = apiResult.errorMessage
            self.data = apiResult.data

    @property
    def data(self):
        return self.__data

    @property
    def errorDesc(self):
        return SaveResult(self.result).name

    @data.setter
    def data(self, data):
        if not data is None:
            self.result = 1
            self.__data = data
        else:
            self.result = 0
            self.__data = None

    @property
    def success(self):
        return self.result == 1