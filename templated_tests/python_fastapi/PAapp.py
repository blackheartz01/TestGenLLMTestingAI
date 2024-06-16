
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema
from typing import List,Optional
from uuid import UUID,uuid4

new_app = FastAPI()

class Task(BaseModel):
    id: Optional[str]= None
    name: str
    balance : int
    account_type: Optional[str]= 'saving'
    Active_User: bool= True

tasks = []

@new_app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Banking application!"}

@new_app.post('/create_user/',response_model=Task)
def create_user(task:Task):
#    task.id=uuid4()
    tasks.append(task)
    return task

@new_app.get('/get_userdetails/',response_model=List[Task])
async def get_userdetails():
    return tasks

@new_app.get('/get_bankbalance/{account_name}',response_model=Task)
def get_bankbalance(account_name:str):
    for task in tasks:
        if task.name == account_name:
            return task
                
    return HTTPException(status_code=404,detail='Task not found')    
