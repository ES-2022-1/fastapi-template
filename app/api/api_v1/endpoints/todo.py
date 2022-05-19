from fastapi import APIRouter, Depends

from app.api import deps
from app.todo.schemas.todo import TodoCreate, TodoView
from app.todo.services.todo import TodoService

router = APIRouter()


@router.post("/", response_model=TodoView)
def create_todo(todo: TodoCreate, service: TodoService = Depends(deps.get_todo_sevice)):
    return service.create(create=todo)
