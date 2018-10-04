class VKError(Exception):

    def __init__(self, code, message, request_params):
        super().__init__(self, message)
        self.code = code
        self.message = message
        self.request_params = request_params
