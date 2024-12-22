from flask import Flask, render_template, request, redirect, url_for
import json
import os

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
    if request.method == "POST":
        # coletar dados do form
        nome = request.form.get("nome")
        qtd = request.form.get("qtd")
        data_validade = request.form.get("dataValidade")

        # criar um novo produto
        novo_produto = {
            "nome": nome,
            "qtd": qtd,
            "dataValidade": data_validade
        }

        # escrever novos dados em produtos_cadastrados.json
        caminho_dir_trab = os.getcwd()
        caminho_arq_json = os.path.join(caminho_dir_trab, "produtos_cadastrados.json")
        
        with open(caminho_arq_json, "r") as arq_json:
            conteudo = json.load(arq_json)
            lista_produtos: list = conteudo["listaProdutos"]
            lista_produtos.append(novo_produto)
        with open(caminho_arq_json, "w") as arq_json:
            json.dump(conteudo, arq_json, indent=4)

        return redirect(url_for("cadastro_compras"))

if __name__ == "__main__":
    app.run(debug=True)