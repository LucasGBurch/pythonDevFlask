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
  global task_id_control # Para dar acesso os id_control declarado fora da função
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", "")) # Ou title=data['title'] na chave direto
  task_id_control += 1 # Contador para id básico nessa API
  tasks.append(new_task)
  print(tasks)
  return jsonify({"message": "Nova tarefa criada com sucesso."}) # Retorno em json, em vez da string direto

# Garantir que subiremos o servidor dessa forma só se executarmos de forma manual.
# Forma recomendada para desenvolvimento local (debug=True em vez de False, quando é em produção):
if __name__ == "__main__":
  app.run(debug=True)
