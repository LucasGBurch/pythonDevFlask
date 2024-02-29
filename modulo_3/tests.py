import pytest
import requests

# TESTES PARA O CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []


# CREATE
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    # Tipo assert response_json['id'] == 1, mas para qualquer criação
    tasks.append(response_json['id'])


# READ ALL
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    responnse_json = response.json()
    assert "tasks" in responnse_json
    assert "total_tasks" in responnse_json


# READ ID
def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']


# PUT
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição da tarefa",
            "title": "Título atualizado",
        }

        # Atualização e retorno da mensagem da requisição
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Nova requisição a tarefa específica, para ver se os valores foram atualizados
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['title'] == payload['title']
        assert response_json['description'] == payload['description']
        assert response_json['completed'] == payload['completed']


# DELETE
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200

        # Tarefa específica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404  # Registro deve ser inexistente após deletar
