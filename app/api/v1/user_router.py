from fastapi import APIRouter,Depends
from app.db.orm import UserOrm
from app.schemas.user import UserSchemas
from app.auth.auth import get_current_user,check_authorization

user = APIRouter(
    tags=['User']
)

@user.post('/api/v1/user/register')
async def create_user(user: UserSchemas):
    result = UserOrm.register_user(user.username,user.password)

    return {'message': 'Users successfull create', 'detail': result}

@user.delete('/api/v1/user/delete')
async def delete_user(user: UserSchemas,current_user: str = Depends(get_current_user), _ = Depends(check_authorization)):


    result = UserOrm.delete_user(user)

    return {'message': 'User delete', 'detail': result}
