class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class NotFoundError(APIException):
    status_code = 404

class AuthenticationError(APIException):
    status_code = 401

class ValidationError(APIException):
    status_code = 422

class PermissionDenied(APIException):
    status_code = 403