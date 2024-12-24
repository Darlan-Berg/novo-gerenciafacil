import random
import string
import json

def gerar_id_prod():
    carac_para_id = string.ascii_letters + string.digits
    id = "".join(random.choice(carac_para_id) for i in range(6))
    return id

def cad_prod_no_json(novo_prod, caminho_arq_json):
    with open(caminho_arq_json, "r") as arq_json:
        conteudo = json.load(arq_json)
        lista_produtos = conteudo["listaProdutos"]
        lista_produtos.append(novo_prod)
    with open(caminho_arq_json, "w") as arq_json:
        json.dump(conteudo, arq_json, indent=4)