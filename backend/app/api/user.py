from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_user(db=db, user_id=user_id)
