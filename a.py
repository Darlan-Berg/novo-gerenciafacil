import json

dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

arquivo = open("dados.json", "w")
json.dump(dados, arquivo)
arquivo.close()

arquivo = open("dados.json", "r")
dados = json.load(arquivo)
arquivo.close()

string_json = '{"nome": "Ana", "idade": 25, "cidade": "Rio de Janeiro"}'
dados = json.loads(string_json)

dados = {
    "nome": "Pedro",
    "idade": 35,
    "cidade": "Belo Horizonte"
}

string_json = json.dumps(dados)

print(type(string_json))