import json

with open("./produtos_cadastrados.json", "r") as arq_json:

    conteudo_antigo = json.load(arq_json)
    print(conteudo_antigo)

    lista_produtos: list = conteudo_antigo["listaProdutos"]
    lista_produtos.append(123)
    lista_produtos.append(456)

    print(conteudo_antigo)