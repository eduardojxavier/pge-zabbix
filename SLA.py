import requests
import json
from datetime import datetime
import requests
import urllib3
import pandas as pd
from datetime import timedelta


ZABBIX_API_URL = 'http://192.168.5.15/zabbix/api_jsonrpc.php'
USERNAME = "Admin"
PASSWORD = "zabbix"

r = requests.post(ZABBIX_API_URL,
                  json={
                        "jsonrpc": "2.0",
                        "method": "user.login",
                        "params": {
                            "username": USERNAME,
                            "password": PASSWORD
                        },
                        "id": 1,
                        
                    })


retorno = requests.post(ZABBIX_API_URL,
                  json={
                        "jsonrpc": "2.0",
                        "method": "sla.getsli",
                        "params": {
                            "slaid": "2",
                        },
                        "id": 1,
                        
                    })



AUTHTOKEN = retorno.json()["result"]

print(AUTHTOKEN)