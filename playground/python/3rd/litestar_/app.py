from dataclasses import dataclass
from typing import Annotated

import msgspec
from litestar import Litestar, get, post
from litestar.di import Provide
from litestar.exceptions import NotFoundException
from litestar.params import Dependency


@dataclass
class TodoItem:
    title: str
    done: bool
    deadline: Annotated[int, msgspec.Meta(ge=1)] | None = None

    def __post_init__(self):
        if self.done and self.deadline is not None:
            raise ValueError("Done tasks cannot have a deadline")


TODO_LIST: list[TodoItem] = [
    TodoItem(title="Start writing TODO list", done=True),
    TodoItem(title="???", done=False),
    TodoItem(title="Profit", done=False),
]


def get_todo_list():
    return TODO_LIST


@post("/")
async def add_item(todo_list: Annotated[list[TodoItem], Dependency], data: TodoItem) -> list[TodoItem]:
    todo_list.append(data)
    return todo_list


def get_todo_by_title(todo_name, todo_list) -> TodoItem:
    for item in todo_list:
        if item.title == todo_name:
            return item
    raise NotFoundException(detail=f"TODO {todo_name!r} not found")


@get("/{item_title:str}")
async def get_item(todo_list: Annotated[list[TodoItem], Dependency], item_title: str) -> TodoItem:
    return get_todo_by_title(item_title, todo_list)


app = Litestar([get_item, add_item], dependencies={"todo_list": Provide(get_todo_list)})
