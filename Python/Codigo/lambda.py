#lambda é uma função que recebe uma variavel e obtem o resultado depois dos dois pontos
#neste caso percorrera a lista e guardara o tamanho de cada item encontrado
contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['gato','cachorro', 'coelho','lebre']
print(contador_letras(lista_animais))

soma = lambda a, b: a+b
print(soma(5,50))

calculadora = {
  'soma': lambda a,b: a+b,
  'subtracao': lambda a,b: a-b,
  'divisao': lambda a,b: a/b,
  'multiplicacao': lambda a,b: a*b,
}

print(type(calculadora))
soma = calculadora ['soma']
subtracao = calculadora ['subtracao']
divisao = calculadora ['divisao']
multiplicacao = calculadora ['multiplicacao']

print('Soma:{}'.format(soma(2,3)))
print('Subtracao::{}'.format(soma(2,3)))
print('Divisao:{}'.format(divisao(2,3)))
print('Multiplicacao:{}'.format(soma(2,3)))