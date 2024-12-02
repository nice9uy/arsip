from datetime import datetime, timedelta, timezone
from typing import Union
from fastapi import Depends, HTTPException
from jose import JWTError, jwt


class ServiceJwt:
    def __init__(self) -> None:
        # self.SECRET_KEY = config.JWT_SECRET
        # self.ALGORITHM = config.JWT_ALGORITHM
        # self.ACCESS_TOKEN_EXPIRE_MINUTES = config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES

        self.SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        self.ALGORITHM  = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def create_access_token(
        self, data: dict, expires_delta: Union[timedelta, None] = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload
        except JWTError as err:
            print(err)
            raise HTTPException(401, "invalid credential")