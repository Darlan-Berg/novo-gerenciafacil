from flask import Flask, render_template, request, redirect, url_for, jsonify
from utils import gerar_id_prod, cad_prod_no_json
import json
import os

app = Flask(__name__)

caminho_dir_trab = os.getcwd()
caminho_arq_json = os.path.join(caminho_dir_trab, "estoque.json")

# ROTA PRINCIPAL
@app.route("/", methods=["GET"])
@app.route("/cadastro-compras", methods=["GET"])
def cadastro_compras():
    return render_template("cadastro_compras.html")



@app.route("/adicionar-produto-no-json", methods=["POST"])
def adicionar_produto_no_json():
    if request.method == "POST":
        # coletar dados do form
        id = gerar_id_prod()
        nome = request.form.get("nome")
        marca = request.form.get("marca")
        qtd = request.form.get("qtd")
        valor_uni = request.form.get("valorUni")
        preco_uni = request.form.get("precoUni")
        data_validade = request.form.get("dataValidade")

        if id and nome and marca and qtd and valor_uni and preco_uni and data_validade:
            # criar um novo produto
            novo_prod = {
                "id": id,
                "nome": nome,
                "marca": marca,
                "qtd": qtd,
                "valorUni": valor_uni,
                "precoUni": preco_uni,
                "dataValidade": data_validade
            }

            cad_prod_no_json(novo_prod, caminho_arq_json)

            return redirect(url_for("cadastro_compras"))
        else:
            return "<h1> Nem todos os dados dos formulários chegaram até o servidor Flask. </h1>"



@app.route("/cadastro-vendas", methods=["GET", "POST"])
def cadastro_vendas():
    if request.method == "GET":
        return render_template("cadastro_vendas.html")



@app.route("/remover-produto-do-json", methods=["POST"])
def remover_produto_no_json():
    if request.method == "POST":
        cont_json_atualizado = request.get_json()
        with open(caminho_arq_json, "w") as arq_json:
            json.dump(cont_json_atualizado, arq_json, indent=4)
            return redirect(url_for("cadastro_vendas"))



@app.route("/retornar-estoque", methods=["GET"])
def retornar_estoque():
    caminho_dir_trab = os.getcwd()
    caminho_arq_json = os.path.join(caminho_dir_trab, "estoque.json")
    
    with open(caminho_arq_json, "r") as arq_json:
        estoque = json.load(arq_json)
        return jsonify(estoque)



@app.route("/estoque", methods=["GET"])
def estoque():
    # carregar o estoque atual
    with open(caminho_arq_json, "r") as arq_json:
        estoque = json.load(arq_json)
        lista_produtos_em_estoque = estoque["listaProdutos"]
    return render_template("estoque.html", lista_produtos_em_estoque=lista_produtos_em_estoque)



if __name__ == "__main__":
    app.run(debug=True)