import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter

from src.application.controllers.users_controller import UsersController
from src.domain.schemas.schemas import UserSchemaInput, UserSchemaOutput
from src.errors.error_handler import handle_error
from src.infra.repositories.user_repository import UserRepository
from src.validators.user_insert_validator import user_insert_validator

router = APIRouter(prefix='/users', tags=['users'])


@router.get(
    '/', response_model=List[UserSchemaOutput], status_code=HTTPStatus.OK
)
def get_users():
    http_response = None
    try:
        user_repository = UserRepository()
        user_controller = UsersController(user_repository)
        http_response = user_controller.get_all_users()
        return http_response
    except Exception as e:
        logging.error('get_users route exception')
        logging.error(e)
        http_response = handle_error(e)
    finally:
        return http_response


@router.post(
    '/', response_model=UserSchemaOutput, status_code=HTTPStatus.CREATED
)
def create_user(user: UserSchemaInput):
    http_response = None
    try:
        user_insert_validator(user.__dict__)
        user_repository = UserRepository()
        user_controller = UsersController(user_repository)
        http_response = user_controller.insert_new_user(user.__dict__)
    except Exception as e:
        logging.error('create_user route exception')
        logging.error(e)
        http_response = handle_error(e)
    finally:
        return http_response


@router.delete(
    '/{user_id}', response_model=UserSchemaOutput, status_code=HTTPStatus.OK
)
def delete_user(user_id: str):
    http_response = None
    try:
        int_user_id = int(user_id)
        user_repository = UserRepository()
        user_controller = UsersController(user_repository)
        http_response = user_controller.delete_user(int_user_id)
    except Exception as e:
        logging.error('delete_user route exception')
        logging.error(e)
        http_response = handle_error(e)
    finally:
        return http_response
