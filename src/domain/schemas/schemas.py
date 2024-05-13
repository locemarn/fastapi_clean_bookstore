from pydantic import BaseModel, EmailStr


class UserSchemaInput(BaseModel):
    email: EmailStr
    password: str
    username: str


class UserSchemaOutput(BaseModel):
    id: int
    email: EmailStr
    username: str
    created_at: str
    updated_at: str
