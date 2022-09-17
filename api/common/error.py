from api.common.response import make_response
from api.common.setting import StatusCode


def bad_request(message):
    make_response(f"Bad request: {message}", StatusCode.ERROR)


def unauthorized(message):
    make_response(f"Unauthoried: {message}", StatusCode.AUTHORIZATION_ERROR)


def forbidden(message):
    make_response(f"Forbidden: {message}", StatusCode.CERTIFICATION_ERROR)
