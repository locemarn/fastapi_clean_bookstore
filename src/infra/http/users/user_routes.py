import logging
from http import HTTPStatus

from fastapi import APIRouter

from src.application.controllers.users_controller import UsersController
from src.application.use_cases.user_insert_use_cases import UserInsertUseCase
from src.domain.repositories.user_repository import UserRepository
from src.domain.schemas.schemas import UserSchemaInput, UserSchemaOutput
from src.errors.error_handler import handle_error
from src.validators.user_insert_validator import user_insert_validator

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/')
async def get_users():
    return {'users': 'get_users'}


@router.post(
    '/', response_model=UserSchemaOutput, status_code=HTTPStatus.CREATED
)
async def create_user(user: UserSchemaInput):
    try:
        user_insert_validator(user.__dict__)
        repository = UserRepository()
        user_case = UserInsertUseCase(repository)
        controller = UsersController(user_case)
        http_response = controller.handler_insert(user)
        return http_response
    except Exception as e:
        logging.error('create_user route exception')
        logging.error(e)
        http_response = handle_error(e)

    print('http_response', http_response)
    return http_response['body'], http_response['status_code']
