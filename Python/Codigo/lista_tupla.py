tupla = (1,2,3,4,5)
#tupla_animal = ('gato', 'cachorro','coelho')
#*****não se consegue alterar o valor de um elemento de uma tupla
#tupla[1] = 12   **** dá erro

lista = [1,2,3,4,5,6,7]
lista_animal = ['gato', 'cachorro','coelho','elefante']

tupla = lista
tupla_animal = tuple(lista_animal)

print('Tupla com numeros:',tupla)

print('Tipo da tupla com animais: ',type(tupla_animal))
print('Tupla com animais: ', tupla_animal)

lista_teste = list(tupla_animal)

print('Tipo da lista teste com animais: ',type(lista_teste))
print('Lista teste com animais: ', lista_teste)

print('Tamanho da tupla com numero: {}'.format(len(tupla)))

print('Lista de numeros: {}'.format(lista))

print('Lista de animais: ', lista_animal)

animal = input("Digite o nome do animal para inserir na lista: ")

if animal in lista_animal:
    opcao= input(animal + " já está na lista!. Deseja excluir? S(sim)/N(nao): ")
    # if  opcao.upper == 'S':
    lista_animal.remove(animal)   
    print('Animal '+animal+" removido")  
else:
    lista_animal.append(animal)
    print('Animal '+animal+" adicionado") 

print('Lista de animais atualizada: ', lista_animal)

opcao= input('Deseja excluir o ultimo animal da lista? S(sim)/N(nao):')
if  opcao == 'S':    
    lista_animal.pop()
    print('Animal excluido!')

print('Lista de animais atualizada: ', lista_animal)  

pos = int(input('Digite a posicao do animal a ser excluido:'))

#print('Tamanho da lista de animais atualizada: {} ',format(len(lista_animal)) )
tam = len(lista_animal)

if  pos< tam:
    lista_animal.pop(pos)
    print('Animal excluido. Lista de animais atualizada: ', lista_animal)

print('Tamanho da lista de animais atualizada: {}'.format(tam))

lista_animal.sort()

print('Lista de animais ordenada crescente: ', lista_animal)

lista.reverse()

print('Lista de numeros decrescente: ', lista)


