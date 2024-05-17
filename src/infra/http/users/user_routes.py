import logging
from http import HTTPStatus
from http.client import HTTPException

from fastapi import APIRouter

from src.application.controllers.users_controller import UsersController
from src.application.use_cases.user_insert_use_cases import UserInsertUseCase
from src.domain.repositories.user_repository import UserRepository
from src.domain.schemas.schemas import UserSchemaInput, UserSchemaOutput

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/')
async def get_users():
    return {'users': 'get_users'}


@router.post(
    '/', response_model=UserSchemaOutput, status_code=HTTPStatus.CREATED
)
async def create_user(user: UserSchemaInput):
    try:
        repository = UserRepository()
        user_case = UserInsertUseCase(repository)
        controller = UsersController(user_case)
        return controller.handler_insert(user)
    except Exception as e:
        logging.error('create_user route exception')
        logging.error(e)
        raise HTTPException(e)
