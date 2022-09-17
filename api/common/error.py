from api.common.response import make_error_response
from api.common.setting import StatusCode


def bad_request(message):
    return make_error_response(message, StatusCode.ERROR)


def unauthorized(message):
    return make_error_response(message, StatusCode.AUTHORIZATION_ERROR)


def forbidden(message):
    return make_error_response(message, StatusCode.CERTIFICATION_ERROR)
