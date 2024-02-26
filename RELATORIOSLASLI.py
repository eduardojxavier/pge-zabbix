import requests
import json

# Parâmetros de autenticação
url = 'http://192.168.5.15/zabbix'
username = 'Admin'
password = 'zabbix'

# Método de autenticação
auth = {
    'jsonrpc': '2.0',
    'method': 'user.login',
    'params': {
        'username': username,
        'password': password,
    },
    'id': 1,
}

# Fazendo a requisição de autenticação
response = requests.post(url, json=auth)
auth_result = response.json()

# Obtendo o token de autenticação
auth_token = auth_result['result']

# Consulta via API usando o método sla.getsli
getsli_params = {
    'jsonrpc': '2.0',
    'method': 'sla.getsli',
    'params': {
        'itemids': '2',  # Substitua pelo ID do item específico
        
    },
    'auth': auth_token,
    'id': 2,
}

# Fazendo a requisição para obter SLI
response = requests.post(url, json=getsli_params)
sli_result = response.json()

# Exibindo o resultado
print(json.dumps(sli_result, indent=4))