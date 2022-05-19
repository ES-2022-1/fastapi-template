from typing import Optional

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    description: str = Field(max_length=50)


class TodoCreate(TodoBase):
    ...


class TodoView(TodoBase):
    ...

    class Config:
        orm_mode = True


class TodoUpdate(BaseModel):
    description: Optional[str] = Field(max_length=50)
