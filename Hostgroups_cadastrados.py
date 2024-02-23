from zabbix_api import ZabbixAPI
import time
from datetime import datetime
import json
import pytz

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


retornoSLA=