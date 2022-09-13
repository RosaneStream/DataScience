from Calculadora1 import Calculadora
from Televisao import Televisao
from contador_letras import contador_letras

if __name__ == 'main':
    tv = Televisao()
    calc = Calculadora(5,10)
    print(tv.ligada)
    print(tv.power())
    print(calc.soma())
    lista = ['cachorro', 'gato', 'coelho']
    total_letras = contador_letras(lista)
    print('Total de letras da lista: {}'.format(total_letras))
