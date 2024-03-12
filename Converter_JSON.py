lista_eventos = [('581310', 'Unavailable by ICMP ping', 'Catraca II', 'Alta', '2024-03-12 10:35:19', '2024-03-12 10:37:19', '0 dias, 0 horas, 2 minutos', 'Não'), ('581312', 'Unavailable by ICMP ping', 'Catraca II', 'Alta', '2024-03-12 10:59:19', '2024-03-12 11:01:19', '0 dias, 0 horas, 2 minutos', 'Não')]


lista_tempo = []

for evento in lista_eventos:
    tempo_indisponibilidade = evento[6]
    dias, horas, minutos = tempo_indisponibilidade.split(', ')
    dias = int(dias.split()[0])
    horas = int(horas.split()[0])
    minutos = int(minutos.split()[0])

    total_horas_indisponibilidade = (dias * 24 * 60) + (horas * 60) + minutos 

    lista_tempo.append(total_horas_indisponibilidade)

print(sum(lista_tempo))
print(lista_tempo)