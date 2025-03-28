from pydantic import BaseModel

class UserSchemas(BaseModel):
    username: str
    password: str
