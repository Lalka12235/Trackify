from pydantic import BaseModel

class UserSchemas(BaseModel):
    username: str
    password: str

class UserOutSchemas(BaseModel):
    id: int
    username:str