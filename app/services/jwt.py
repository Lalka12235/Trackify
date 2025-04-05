import jwt
from datetime import datetime,timedelta
from fastapi import HTTPException,status

SECRET_KEY = ''
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 15



def encode_jwt(
        payload,secret_key,algorithm,expire_mitutes=ACCESS_TOKEN_EXPIRE_MINUTES
):
    expired = datetime.utcnow() +timedelta(minutes=expire_mitutes)
    payload.update({'exp': expired})
    token = jwt.encode(payload,secret_key,algorithm=algorithm)
    return token 


def decode_jwt(
        token,
        secret_key,
        algorithm,
):
    try:
        decode = jwt.decode(token,secret_key,algorithms=[algorithm])
        return decode
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
