from cerberus import Validator

from src.errors.types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def user_insert_validator(user):
    body_validator = Validator({
        'username': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 50,
            'required': True,
            'empty': False,
        },
        'password': {
            'type': 'string',
            'minlength': 6,
            'maxlength': 50,
            'required': True,
            'empty': False,
        },
        'email': {
            'type': 'string',
            'maxlength': 50,
            'required': True,
            'empty': False,
            'regex': r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',
        },
    })
    response = body_validator.validate(user)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
