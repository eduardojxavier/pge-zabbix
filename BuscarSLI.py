from zabbix_api import ZabbixAPI
import time
from datetime import datetime
import json
import pytz
import pandas as pd

URL = 'http://192.168.5.15/zabbix'
USERNAME = 'Admin'
PASSWORD = 'zabbix'

try:
    zapi = ZabbixAPI(URL, timeout=180)
    zapi.login(USERNAME,PASSWORD)
    print('Conectado com sucesso!')

except Exception as erro:
    print(f'Não foi possível conectar-se. {erro}')
    exit()



retornoSLA = zapi.event.get({'output':['eventid','name','host','severity','clock','r_eventid'],
                                    'selectHosts':['hostid','host'],
                                    'time_from': 1708686000,
                                    'time_till': 1708700400,
                                    'acknowledges': 1
                                    })

print(retornoSLA)