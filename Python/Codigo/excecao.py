lista = [1,10]
arquivo = open('notas.txt')
try
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]
    #x=a erro para variavel não existente
    # arquivo.close precisa ser executado no finally
except ZeroDivisionError:
    print('Não é possível dividir por 0')
except ArithmeticError:
    print('Erro em operação aritmetica')
except IndexError:
    print('Indice não existe')
except BaseException as erro:
    print('Erro desconhecido {}'.format(erro))
else:
    print('Operacao realizada com sucesso')
finally:
    arquivo.close()