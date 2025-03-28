from fastapi import APIRouter,HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.user import UserSchemas

auth = APIRouter(
    tags=['Auth']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')

