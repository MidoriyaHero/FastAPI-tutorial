from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4, UUID
from fastapi.responses import HTMLResponse


app = FastAPI()
db: List[User] =[
    User(id = uuid4(), 
         name = 'Tin',
         gender = Gender.male,
         role = [Role.admin],), 

    User(id = uuid4(), 
         name = 'Tindeptrain',
         gender = Gender.female,
         role = [Role.user, Role.admin],),
]

@app.get('/',response_class = HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Fast API</h1>
            <p>Go to: 127.0.0.1:8000/docs</p>
        </body>
    </html>
    """

@app.get('/api/users/v1')
async def fetch_users():
    return db


@app.post('/api/users/v1')
async def add_user(user: User):
    db.append(user)
    return 'user added'