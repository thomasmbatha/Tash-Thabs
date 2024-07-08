from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Category(Enum):
    PERSONAL = 'personal'
    WORK = 'work'

class Todo(BaseModel):
    title: str
    completed: bool
    id: int
    category: Category

todos = {
    0: Todo(title='test1', completed=True, id=0, cartegory=Category.PERSONAL),
    1: Todo(title='test2',completed=False, id=1, category=Category.WORK),
}
@app.get('/')
def index() -> dict[str, dict[int, Todo]]:
    return {'todos':todos}

#6:47 / 26:54 FastAPI Crash Course: Building Robust APIs with Python for Beginners