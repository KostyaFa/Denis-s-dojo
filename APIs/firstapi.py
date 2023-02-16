from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str

dict_id = dict()

@app.get('/user/{id}')
async def read_item(id: int, item: User):
    if dict_id.get(id) == None:
        return 'Пользователь отсутсвует'
    else: 
        return dict_id.get(id).name

@app.post('/user/{id}')
async def create_item(id: int, item: User):
    dict_id[id] = item
    return 'Добавлен элемент {id}!'

@app.put('/user/{id}')
async def update_item(id: int, item: User):
    if dict_id.get(id) != None:
        dict_id[id] = item
        return 'Элемент {id} обновлен!'

@app.delete('/user/{id}')
async def delete_item(id: int, item: User):
    if dict_id.get(id) == None:
        return 'Удалять нечего'
    else:
        del dict_id[id]
        return 'Элемент {id} удален!'
