from fastapi import Depends, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from jose import jwt , JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta
import secrets
from fastapi.templating import Jinja2Templates
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)


templates = Jinja2Templates(directory="frontend_api/fluxos/auth")
class Config:
    SECRET_KEY = "W988@#8W#Egpqwcv(*)"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8


def create_access_token(sub: str, id: str, role: str, expires_delta = datetime.utcnow() + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = {"sub": sub, "id": id, "role": role}
    return jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)

def validate_token(request: Request):
    token = request.cookies.get("access_token")
    if token is None:
        raise HTTPException(status_code=302, headers={"Location": "/login"})
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=302, headers={"Location": "/login"})
    
def verify_password(plain_password, hashed_password):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(plain_password, hashed_password)


