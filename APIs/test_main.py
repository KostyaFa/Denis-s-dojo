from fastapi.testclient import TestClient

from firstapi import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        '/user/3',
        json = {'name': 'Den4ik'}                  
        )
    assert response.status_code == 200
    assert 'Добавлен пользователь с id = 3'

def test_create_having_item():
    response = client.post(
        '/user/1',
        json = {'name': 'Den4ik'}                  
        )
    assert response.status_code == 200
    assert 'Пользователь с id = 1 уже существует'
    
def test_read_all():
    responce = client.get(
        '/user'
        )
    assert responce.status_code == 200
    assert 'Пользователей нет'

def test_delete_all():
    responce = client.delete(
        '/user'
        )
    assert responce.status_code == 200
    assert 'Пользователей нет'
    
# def test_read_one():
#     responce = client.get(url="/user/1"    
#         )
#     assert responce.status_code == 200
#     assert responce.json() == {'name': 'Den4ik'}
    
