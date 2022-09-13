class Error(Exception):
    pass

class MeuErro(Error):
    def __int__(self, mensagem):
        self.mensagem = mensagem

while True:
    try:
        nota1 = int(input('Digite a primeira nota: '))
        print (nota1)
        if nota1>10 or nota1<0:
            raise MeuErro('Digite um número de 0 a 10')
        break
    except ValueError:
        print('Valor invalido. Digite um número')
    except MeuErro as ex:
        print(ex)

