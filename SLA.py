import json
import requests

# Configurações de conexão
# url = 'http://192.168.70.120/zabbix/api_jsonrpc.php'
# username = 'eduardo.filho'
# password = 'Dudu@242255'

url = 'http://192.168.5.15/zabbix/api_jsonrpc.php'
username = 'Admin'
password = 'zabbix'

# Autenticação
headers = {'Content-Type': 'application/json-rpc'}
payload = {
    'jsonrpc': '2.0',
    'method': 'user.login',
    'params': {
        'username': username,
        'password': password,
    },
    'id': 1
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
token = response.json()['result']

# Método sla.get
payload_sla = {
    'jsonrpc': '2.0',
    'method': 'event.get',
    'params': {
        # 'slaid': '2',
        # 'serviceids':[
        #     1,
        #     2,
        #     3
        # ],
        # 'periods': 3,
        
    },
    'auth': token,
    'id': 1
}

response_sla = requests.post(url, data=json.dumps(payload_sla), headers=headers)
sla_data = response_sla.json()

# Imprimindo o resultado
print(json.dumps(sla_data, indent=4))
