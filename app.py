from fastapi import FastAPI

from src.infra.http.users import user_routes

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


app.include_router(user_routes.router)
