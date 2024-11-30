from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from core.config import settings
from db.session import engine
from db.base import Base
from pydantic import BaseModel
from db.session import SessionLocal

from schemas.user import UserCreate, ShowUser
from db.repository.user import create_new_user


def create_tables():
   Base.metadata.create_all(bind=engine)

def start_application():
   app = FastAPI(
      title=settings.PROJECT_NAME, 
      version=settings.PROJECT_VERSION
      )
   create_tables()
   return app

templates = Jinja2Templates(directory="templates")
app = start_application()
app.mount("/static", StaticFiles(directory="templates/static"), name="style")

class User(BaseModel):
   username: str
   password: str
   email: str
    
@app.get("/register", response_class=HTMLResponse)
async def send_register(request: Request):
   return templates.TemplateResponse("registration.html",{"request": request})
    
@app.post("/register")
async def register(user: User):
   user = UserCreate(login=user.username, email=user.email, password=user.password)
   print(f"Получен пользователь: {user}")
   create_new_user(user, SessionLocal)
   return {"message": "Регистрация успешна!"}


'''
@router.post('/sign_in', response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user : UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
'''