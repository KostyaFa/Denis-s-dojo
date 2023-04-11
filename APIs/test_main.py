from fastapi.testclient import TestClient
from firstapi import app

client = TestClient(app)


def test_create_item():
    responce = client.post('/user/3', json = {'name' : 'Den4ik'})
    assert responce.json() == 'Добавлен пользователь с id = 3'

def test_create_having_item():
    responce = client.post('/user/3', json = {'name' : 'Ven4ik'})
    assert responce.json() == 'Пользователь с id = 3 уже существует'

def test_get_exist_item():
    responce = client.get('/user/3')
    assert responce.json() == 'Den4ik'

def test_get_no_exist_item():
    responce = client.get('/user/4')
    assert responce.json() == 'Пользователя с id = 4 не существует'

def test_get_all():
    responce = client.get('/user')
    assert responce.json() == {'3' : {'name' : 'Den4ik'}}

def test_put_new_item():
    responce = client.put('/user/3', json={'name' : 'Ven4ik'})
    assert responce.json() == 'Обновлены данные пользователя с id = 3'

def test_put_old_item():
    responce = client.put('/user/3', json={'name' : 'Ven4ik'})
    assert responce.json() == 'Данные пользователя с id = 3 остались без изменений'

def test_put_no_exist_item():
    responce = client.put('/user/4', json={'name' : 'Ven4ik'})
    assert responce.json() == 'Пользователя с id = 4 не существует'

def test_del_item():
    responce = client.delete('/user/3')
    assert responce.json() == 'Пользователь с id = 3 удален'

def test_del_no_exist_item():
    responce = client.delete('/user/3')
    assert responce.json() == 'Пользователя с id = 3 не существует'

def test_get_all_no_exist():
    responce = client.get('/user')
    assert responce.json() == 'Пользователей нет'

def test_del_all_no_exist():
    responce = client.delete('/user')
    assert responce.json() == 'Пользователей нет'

def test_del_all():
    client.post('/user/3', json = {'name' : 'Den4ik'})
    client.post('/user/4', json = {'name' : 'Ven4ik'})

    # responce = client.get('/user')
    # assert responce.json() == {'3' : {'name' : 'Den4ik'}, '4' : {'name': 'Ven4ik'}}
    #  >>> OK

    responce = client.delete('/user')
    assert responce.json() == 'Данные всех пользователей удалены'

    responce = client.get('/user')
    assert responce.json() == 'Пользователей нет'