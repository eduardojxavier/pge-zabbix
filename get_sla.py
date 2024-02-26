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
    "auth": "DIGITE SEU TOKEN",
    "id": 1
}

response = requests.post(url, json=payload, headers=headers, verify=False)

if response.status_code == 200:
    data_dict = response.json()['result']
    periods = data_dict['periods']
    service_ids = data_dict['serviceids']
    sli = data_dict['sli']

    rows = []
    for idx, sli_item in enumerate(sli):
        period = periods[idx]
        period_from = period['period_from']
        period_to = period['period_to']
        service_ids_period = service_ids[:len(sli_item)] 

        for i, sli_data in enumerate(sli_item):
            service_id = service_ids_period[i]
            uptime = sli_data['uptime']
            downtime = sli_data['downtime']
            sli_value = sli_data['sli']
            error_budget = sli_data['error_budget']
            excluded_downtimes = sli_data['excluded_downtimes']
            critico = "Não Crítico"
            meta = "97"

            period_from = pd.to_datetime(period_from, unit='s')
            period_to = pd.to_datetime(period_to, unit='s')
            uptime = str(timedelta(seconds=uptime))
            downtime = str(timedelta(seconds=downtime))

            row = {

                'Period From': period_from,
                'Period To': period_to,
                #'Hours': Hours,
                #'Period': period,
                'Service ID': service_id,
                'Uptime': uptime,
                'Downtime': downtime,
                'SLI': sli_value,
                'Error Budget': error_budget,
                'Excluded Downtimes': excluded_downtimes,
                'Criticidade':critico,
                'Meta':meta
            }
            rows.append(row)

    df = pd.DataFrame(rows)
    print(df)