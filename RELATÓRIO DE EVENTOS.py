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


def get_history(): #Função para saber quando a trigger disparou

    dataInicio = 1708686000
    dataFim = 1708743480

    lista_eventos = []  #lista para guardar os eventos onde r_eventid não seja 0.
    lista_duracao = [] 
    # teste = 136191

    fuso_horario_recife = pytz.timezone('America/Recife')

    abertura_evento = zapi.event.get({'output':['eventid','name','host','severity','clock','r_eventid'],
                                    'selectHosts':['hostid','host'],
                                    'time_from': dataInicio,
                                    'time_till': dataFim})#"eventids": 136191 "eventids": teste
    

    eventid = 'eventid' 
    name = 'name'
    horaInicioEvento = 'clock'
    r_eventid = 'r_eventid'
    severity = 'severity'
    host = 'host'

    #converter o json em uma lista de dicionários
    converter_json = json.dumps(abertura_evento)
    dicionario_abertura_evento = json.loads(converter_json)

    #Testar se o evento está com r_eventid preenchido
    for i in dicionario_abertura_evento:

        id_inicio_evento = i[eventid]
        severidade_evento = i[severity]


        if i[r_eventid] != '0' and (i[severity] == '4' or i[severity] == '5'): 
            lista_eventos.append(i)
            # print (lista_eventos)
            
            for j in lista_eventos:
                converte_hora = int(j['clock'])
                data_hora = datetime.fromtimestamp(converte_hora,fuso_horario_recife)
                horaInicio = data_hora.strftime('%d-%m-%Y %H:%M:%S')
                
                #Atribui cada posição do dicionário a uma variável
                id_retorno_evento = j['r_eventid']
                nome_evento = j['name']
                severidade_evento = j['severity']
                host_evento = j['hosts'][0]['host']
                
                
                fechamento_evento = zapi.event.get({"output":['clock'],
                                                    "eventids": id_retorno_evento})
                
                converter_json_fechamento = json.dumps(fechamento_evento)
                dicionario_fechamento_evento = json.loads(converter_json_fechamento)
                for k in dicionario_fechamento_evento:
                    converte_hora_fechamento = int(k['clock'])
                    data_hora_fechamento = datetime.fromtimestamp(converte_hora_fechamento, fuso_horario_recife)
                    horaFinal = data_hora_fechamento.strftime('%d-%m-%Y %H:%M:%S')

            duracaoEvento = data_hora_fechamento - data_hora        
            
            # print(id_inicio_evento, nome_evento, host_evento, severidade_evento, horaInicio, horaFinal, duracaoEvento) 
            print(host_evento, nome_evento, severidade_evento, horaInicio, horaFinal, duracaoEvento)                
            



print(get_history())
