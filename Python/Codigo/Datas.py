from datetime import date, time, datetime, timedelta

def manipula_date():
    data_atual = date.today()
    print(data_atual)
    data_atual_str = data_atual.strftime('%d/%m/%y')
    print(data_atual_str)
    #dia da semana, nome do mes e ano com 4 digitos
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual_str))
    print(type(data_atual))

def manipula_time():
    horario = time(hour=19,minute=15,second=43)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

def manipula_datetime():
    datahora_atual = datetime.now()
    print(datahora_atual)
    print(type(datahora_atual))
    datahora_str = datahora_atual.strftime('%d/%m/%y - %H:%M:%S')
    print(datahora_str)
    datahora_str = datahora_atual.strftime('%c')
    print(datahora_str)
    #dia do mes
    print(datahora_atual.day)
    # hora atual
    print(datahora_atual.hour)
    # numero do mes
    print(datahora_atual.month)
    #numero do dia da semana
    print(datahora_atual.weekday())
    tupla_dias = ('Segunda','Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado','Domingo')
    #imprime o dia da semana na ordem que está na tupla
    print(tupla_dias[datahora_atual.weekday()])
    data_criada = datetime(1968, 11, 29, 19, 44, 40)
    print(data_criada.strftime('%c'))
    data_string = '29/11/1968'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))

def diferenca_datas():
    datahora_atual = datetime.now()
    print(datahora_atual)
    datahora_str = datahora_atual.strftime('%d/%m/%y')
    print(datahora_str)
    #um ano atras
    nova_data = datahora_atual + timedelta(days=365, hours=4, minutes=2)
    print(nova_data)

if __name__ == '__main__':
    #manipula_time()
    #manipula_date()
    #manipula_datetime()
    diferenca_datas()