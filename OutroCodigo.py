import requests
import urllib3
import pandas as pd
from datetime import timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "http://192.168.5.15/zabbix"
headers = {
    "Content-Type": "application/json"
}

payload = {
    "jsonrpc": "2.0",
    "method": "sla.getsli",
    "params": {
        "slaid": "2",
    },
    "auth": "24c94acda232f176de650448b7201b4d320d1048b137711d79677d9ddf1f9fdb",
    "id": 1
}

r = requests.post(url, json=payload, headers=headers, verify=False)

teste = r.json()["result"]

print (teste)