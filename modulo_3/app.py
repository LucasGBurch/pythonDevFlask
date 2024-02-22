from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

@app.route("/") # / é a clássica rota inicial
def hello_world():
  return "Hello world!"

@app.route("/about")
def about():
  return "Página sobre"

# Garantir que subiremos o servidor dessa forma só se executarmos de forma manual.
# Forma recomendada para desenvolvimento local:
if __name__ == "__main__":
  app.run(debug=True)
