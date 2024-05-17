from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def handle_error(error: Exception):
    if isinstance(error, (HttpUnprocessableEntityError, HttpNotFoundError)):
        return {
            'status_code': error.status_code,
            'message': str(error),
            'body': {
                'errors': [{'title': error.name, 'detail': error.message}]
            },
        }

    return {
        'status_code': 500,
        'message': str(error),
        'body': {
            'errors': [
                {'title': 'Internal Server Error', 'detail': str(error)}
            ]
        },
    }
