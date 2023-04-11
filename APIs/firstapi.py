from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str

dict_id = dict()


@app.get('/user/{id}')
async def read_item(id: int):
    if dict_id.get(id):
        return dict_id.get(id).name
    return f'Пользователя с id = {id} не существует'
    
@app.get('/user')
async def read_all():
    if  dict_id:
        return dict_id
    return 'Пользователей нет'
    
@app.post('/user/{id}')
async def create_item(item: User, id: int):
    if dict_id.get(id):
        return f'Пользователь с id = {id} уже существует'
    dict_id[id] = item
    return f'Добавлен пользователь с id = {id}'

@app.put('/user/{id}')
async def update_item(item: User, id: int):
    if dict_id.get(id):
        temp = dict_id[id]
        dict_id[id] = item
        if dict_id[id] == temp:
            return f'Данные пользователя с id = {id} остались без изменений'
        return f'Обновлены данные пользователя с id = {id}'
    return f'Пользователя с id = {id} не существует'

@app.delete('/user/{id}')
async def delete_item(id: int):
    if dict_id.get(id):
        del dict_id[id]
        return f'Пользователь с id = {id} удален'
    return f'Пользователя с id = {id} не существует'  
    
@app.delete('/user')
async def delete_all():
    if dict_id:
        dict_id.clear()
        return 'Данные всех пользователей удалены'
    return 'Пользователей нет'