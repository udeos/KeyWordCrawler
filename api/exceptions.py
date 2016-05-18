class BadRequestError(Exception):
    def __init__(self, code, message, type):
        self.code = code
        self.message = message
        self.type = type

    def __str__(self):
        return 'Bad Request: code=%s type=%s message=%s' % (
            self.code, self.type, self.message
        )
