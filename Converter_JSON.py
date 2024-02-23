import json

dados = """
    [{"eventid": "1"}, {"eventid": "4"}, {"eventid": "10"}, {"eventid": "20"}, {"eventid": "32"}, {"eventid": "33"}]
"""

# Converter a string JSON em uma lista de dicionários
lista_de_dicionarios = json.loads(dados)

# Acessar a chave 'eventid' para cada dicionário na lista
chave_desejada = "eventid"
valores = [dicionario[chave_desejada] for dicionario in lista_de_dicionarios]

print(valores)
