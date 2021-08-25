from fastapi import APIRouter, Depends

from schemas.account import UserOutSchema, UserInSchema
from services.account import AccountService
from config.database import get_db, Session

router = APIRouter(prefix="/account")


@router.post('/sign-up/', response_model=UserOutSchema)
def sing_up(profile: UserInSchema, db: Session = Depends(get_db)):
    account_service = AccountService(db=db)
    user = account_service.sign_up(profile)
    return user


@router.post('/sign-in/', response_model=UserOutSchema)
def sing_in(profile: UserInSchema, db: Session = Depends(get_db)):
    account_service = AccountService(db=db)
    user = account_service.sign_in(profile)
    return user
