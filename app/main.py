from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
import time

from app.database import get_db, engine, Base
from app.models import UserDB, PortfolioDB, FavoriteDB, AlertDB
from app.auth import get_password_hash, verify_password, create_access_token, get_current_user

app = FastAPI(title="CryptoWatch API", version="1.0.0")

# Разрешаем CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# --- Схемы Pydantic ---
class UserRegister(BaseModel):
    login: str
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    login: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    name: str
    login: str
    email: str

# --- Эндпоинты аутентификации ---
@app.post("/api/v1/auth/register", response_model=Token)
async def register(user_data: UserRegister, db: AsyncSession = Depends(get_db)):
    existing = await db.execute(select(UserDB).where(UserDB.login == user_data.login.lower()))
    if existing.scalars().first():
        raise HTTPException(status_code=400, detail="Логин уже занят")
    
    hashed_pw = get_password_hash(user_data.password)
    new_user = UserDB(
        login=user_data.login.lower(),
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_pw,
        created=int(time.time() * 1000)
    )
    db.add(new_user)
    await db.commit()
    
    access_token = create_access_token(data={"sub": new_user.login})
    return {
        "access_token": access_token, 
        "token_type": "bearer", 
        "name": new_user.name, 
        "login": new_user.login, 
        "email": new_user.email
    }

@app.post("/api/v1/auth/login", response_model=Token)
async def login(form_data: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserDB).where(UserDB.login == form_data.login.lower()))
    user = result.scalars().first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    
    access_token = create_access_token(data={"sub": user.login})
    return {
        "access_token": access_token, 
        "token_type": "bearer", 
        "name": user.name, 
        "login": user.login, 
        "email": user.email
    }

@app.get("/api/v1/auth/me")
async def get_me(current_user: UserDB = Depends(get_current_user)):
    return {
        "login": current_user.login,
        "name": current_user.name,
        "email": current_user.email,
        "created": current_user.created
    }