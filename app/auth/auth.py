from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.auth_schemas import UserLoginSchema,TokenSchema
from app.services.jwt import encode_jwt,decode_jwt
from app.services.hash import verify_pass
from app.db.orm import UserOrm

auth = APIRouter(
    tags=['Auth']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')



def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt(token)
        user_id = payload.get('sub')
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate credeantials'
            )
        return user_id
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credeantials'
        )
    

def check_authorization(username: str, current_user: str = Depends(get_current_user)):
    if username != current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Not authorized'
        )
    


@auth.get('/token',response_model=TokenSchema)
async def  login_for_access_token(form_data: UserLoginSchema):
    user = UserOrm.select_user(form_data.username)

    if not user or not verify_pass(form_data.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password'
        )
    
    access_token = encode_jwt(data={'sub': user.id})
    return {'access_token': access_token,'token_type': 'bearer'}