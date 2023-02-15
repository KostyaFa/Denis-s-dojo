# импорт библиотек 

from fastapi import FastAPI
from pydantic import BaseModel

# создаем приложение
app = FastAPI()

# создаем User класс
class User(BaseModel):
    name : str
# словарь, для хранения User'ов
dict_id = dict()

# запрос get 
@app.get('/user/{id}')
async def read_item(id: int, item: User):
    if dict_id.get(id) == None:
        return f"Пользователь отсутсвует"
    else: 
        return dict_id.get(id).name
# запрос post
@app.post('/user/{id}')
async def create_item(id: int, item: User):
    dict_id[id] = item
    return f"Добавлен элемент {id}!"

# запрос put
@app.put('/user/{id}')
async def update_item(id: int, item: User):
    if dict_id.get(id) == None:
        return f'Обновлять нечего'
    else: 
        dict_id[id] = item
        return f"Элемент {id} обновлен!"
# запрос delete
@app.delete('/user/{id}')
async def delete_item(id: int, item: User):
    if dict_id.get(id) == None:
        return f'Удалять нечего'
    else:
        del dict_id[id]
        return f"Элемент {id} удален!"
