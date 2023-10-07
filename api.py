from fastapi import FastAPI, APIRouter, Body

# from pydantic import BaseModel, ValidationError, field_validator

app = FastAPI()  # create an instance of FastAPI

router = APIRouter()  # create an instance of router


@router.get("/")
def hello_world() -> dict:
    # TODO
    return {"hello": "world"}


@router.get("/items2/")
def read_item(item_id: int = None):
    # TODO
    return {"item_id": item_id}


@router.post("/")
def add(task: str = Body()):
    task_list.append({"task": task, "status": StatusType.PENDING})
    print(task_list)
    return task_list


app.include_router(router)  # add the router to the FastAPI instance
