from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()


class People(BaseModel):
    name: str
    age: int
    address: str
    salary: float


@app.post('/insert')
def insert(people: People):
    age_after_10_years = people.age + 10
    msg = f'此人名字叫做：{people.name}，十年后此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}


@app.get('/')
def index():
    return {'message': '你已经正确创建 FastApi 服务！'}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == 'lenet':
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get('/files/{file_path:path}')
async def read_user_me(file_path: str):
    return {'file_path': file_path}
