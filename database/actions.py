from datetime import timedelta, datetime
from jose import jwt
from contains.variables import pwd_context
from core.config import settings
from database.db import f_db
from core.ds import UserInDb


def verify_pwd(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)


def get_pwd_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    for user in f_db["users"]:
        if user["username"] == username:
            return UserInDb(**user)


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_pwd(password, user.hashed_pwd):
        return False

    return user


def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow()

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

