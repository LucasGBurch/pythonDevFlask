import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []


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


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    responnse_json = response.json()
    assert "tasks" in responnse_json
    assert "total_tasks" in responnse_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']
