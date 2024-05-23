from http import HTTPStatus

from fastapi import FastAPI

from src.infra.http.users import user_routes

app = FastAPI()

app.include_router(user_routes.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=dict[str, str])
async def root():
    return {'message': 'Hello World'}
