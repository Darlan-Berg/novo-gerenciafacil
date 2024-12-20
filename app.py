from flask import Flask, render_template, request
print(__file__)
app = Flask(__name__)

# ROTA PRINCIPAL
@app.route("/", methods=["GET"])
@app.route("/cadastro-compras", methods=["GET"])
def cadastro_compras():
    return render_template("cadastro_compras.html")

# ROTA PARA RECEBER OS DADOS DO FORMULÁRIO DE cadastro_compras.html
# E COLOCA-LOS NO ARQUIVO JSON
@app.route("/adicionar-produto-no-json", methods=["POST"])
def adicionar_produto_no_json():
    # caminho do arquivo: /home/aluno/Documentos/novo-gerenciafacil/produtos_cadastrados.json
    pass

if __name__ == "__main__":
    app.run(debug=True)