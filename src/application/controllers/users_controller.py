from src.application.controllers.controller_interface import (
    ControllerInterface,
)
from src.application.use_cases.UseCaseInterface import UseCaseInterface
from src.domain.schemas.schemas import UserSchemaInput


class UsersController(ControllerInterface):
    def __init__(self, user_use_case: UseCaseInterface):
        self.__user_use_case = user_use_case

    def handler_insert(self, user: UserSchemaInput) -> dict[str, str | int]:
        response = self.__user_use_case.execute(user.__dict__)
        return response
