import os
import hmac
import hashlib
import typing

from config.auth import sign_jwt
from models.account import User
from schemas.account import UserSchema, UserCreateSchema
from schemas.account import UserInSchema
from exceptions.account import AccountException

from .base import BaseCRUD, BaseService, Session


class AccountCRUD(BaseCRUD):
    model = User

    def get(self, token: str = None, pk: int = None, email: str = None) -> typing.Optional[model]:
        query = None
        if token:
            query = self.db.query(self.model).filter(self.model.token == token)
        elif pk:
            query = self.db.query(self.model).filter(self.model.id == pk)
        elif email:
            query = self.db.query(self.model).filter(self.model.email == email)
        if not query:
            return None
        return query.first()


class AccountService(BaseService):
    output_schema = UserSchema
    create_schema = UserCreateSchema

    def __init__(self, db: Session):
        self.objects = AccountCRUD(db)

    def sign_up(self, user: UserInSchema) -> output_schema:
        existing_user = self.objects.get(email=user.email)
        if existing_user:
            raise AccountException.UserCreate()
        jwt_token = sign_jwt(user.email)['access_token']
        _salt, _hash = self.hash_new_password(user.password)
        obj = self.create_schema(**user.dict(), password_hash=_hash, password_salt=_salt, token=jwt_token)
        return self.objects.create(obj)

    def sign_in(self, user: UserInSchema) -> output_schema:
        existing_user = self.objects.get(email=user.email)
        if existing_user is None:
            raise AccountException.Authorize()
        if not self.is_correct_password(existing_user.password_salt, existing_user.password_hash, user.password):
            raise AccountException.Authorize()
        return existing_user

    @staticmethod
    def hash_new_password(password: str) -> typing.Tuple[bytes, bytes]:
        """
        Hash the provided password with a randomly-generated salt and return the
        salt and hash to store in the database.
        """
        salt = os.urandom(16)
        pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt, pw_hash

    @staticmethod
    def is_correct_password(salt: bytes, pw_hash: bytes, password: str) -> bool:
        """
        Given a previously-stored salt and hash, and a password provided by a user
        trying to log in, check whether the password is correct.
        """
        return hmac.compare_digest(
            pw_hash,
            hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        )
