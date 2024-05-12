from http.client import HTTPException

from fastapi import APIRouter

router = APIRouter(prefix='/users', tags=['users'])


# @router.get("/users", response_model=List[schemas.User])
@router.get('/')
async def get_users():
    return {'users': 'get_users'}


@router.post('/')
async def create_user():
    try:
        ...
    except Exception:
        raise HTTPException(status_code=404, detail='User not found')
