#Conjunto - tipo SET elimina duplicação de valores
conjunto = {1,2,3,4,5,6,7}
conjunto_2 = {4,5,6,7,8,9,10}
conjunto_animal = {'gato','cachorro','papagaio'}
conjunto_ani = {'gato','rato'}

print(type(conjunto))
print('Conjunto: {}'.format(conjunto))
conjunto.discard(2)
print('Conjunto sem o 2: {}'.format(conjunto))
conjunto.add(2)
print('Conjunto adicionando o 2: {}'.format(conjunto))
conjunto_uniao = conjunto.union(conjunto_2)
print('Conjunto uniao numeros: {}'.format(conjunto_uniao))
conjunto_diferente = conjunto.difference(conjunto_2)
print('Conjunto numeros que só constam no primeiro conjunto:{}'.format(conjunto_diferente))
conjunto_diferente = conjunto_2.difference(conjunto)
print('Conjunto numeros que só constam no segundo conjunto:{}'.format(conjunto_diferente))
conjunto_diferente = conjunto_2.symmetric_difference(conjunto)
print('Conjunto resultado da diferenca entre os dois conjuntos: {}'.format(conjunto_diferente))
conjunto_uniao = conjunto.intersection(conjunto_2)
print('Conjunto interseccao numeros: {}'.format(conjunto_uniao))
print(conjunto_animal)
conjunto_animal.add('coelho')
print(conjunto_animal)
conjunto_uniao_ani = conjunto_ani.union(conjunto_animal)
print('Conjunto uniao animais: ')
print(conjunto_uniao_ani)
conj_a = {1,2,3}
conj_b = {1,2,3,4,5,6,7,8,9,0}
contido = conj_a.issubset(conj_b)
print('A é um subconjunto de B: ',contido)
contido = conj_b.issuperset(conj_a)
print('B é um superconjunto de A: ',contido)
print(conj_a)
print(conj_b)

#é possivel transformar lista em SET e vice-versa
lista_a = list(conjunto)
conj_teste = set(lista_a)

print('Lista: ')
print(type(lista_a))
print(conjunto)

print('Set: ')
print(type(conj_teste))
print(conj_teste)