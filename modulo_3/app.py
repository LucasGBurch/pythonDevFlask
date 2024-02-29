from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)

# CRUD - Create Read Update Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control  # Para dar acesso os id_control declarado fora da função
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get(
        "description", ""))  # Ou title=data['title'] na chave direto
    task_id_control += 1  # Contador para id básico nessa API
    tasks.append(new_task)
    # print(tasks)
    # Retorno em json, em vez da string direto
    return jsonify({"message": "Nova tarefa criada com sucesso.", "id": new_task.id})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]  # Método da classe Task
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    # Se não tiver nenhuma correspondência, retorna o erro:
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

# EXEMPLO DE PARÂMETRO PARA ROTAS
# @app.route('/user/<int:user_id>')
# def show_user(user_id):
#     print(user_id)
#     print(type(user_id))
#     # Formatando este retorno pra string, já que fizemos que a rota receba inteiros
#     return "%s" % user_id


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break  # Para não precisar seguir procurando quando encontrar, para não gastar processamento desnecessariamente e ter código mais performático

    # print(task)
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    # print(task)
    # , 200, de sucesso da requisição, já é o padrão do jsonify
    return jsonify({"message": "Tarefa atualizada com sucesso."})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        # print(task)
        if t.id == id:
            # Não remover diretamente com pop(), pois alteraria o tamanho da lista!
            task = t
            break  # Para não precisar seguir procurando quando encontrar, para não gastar processamento desnecessariamente e ter código mais performático

    if not task:  # task == None
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso."})


# Garantir que subiremos o servidor dessa forma só se executarmos de forma manual.
# Forma recomendada para desenvolvimento local (debug=True em vez de False, quando é em produção):
if __name__ == "__main__":
    app.run(debug=True)
