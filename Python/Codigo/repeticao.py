# a = int(input('Digite um numero:'))

# #percorre de 1 até o numero digitado mais 1
# for num in range(a+1):
#     print('a:', a)
#     div = 0

#     for x in range(1, num+1):
#         resto = num % x
#         print('x: ', x)
#         print('resto: ', resto)
#         if resto == 0:
#             div +=1
#             print('div: ', div)  
#             if div == 2:
#               print('É primo:', num) 
#             else: print('Não é primo:', num)


a = int(input('Primeiro bimestre:'))

while a>10:
    a = int(input('Você digitou errado. Primeiro bimestre:'))

b = int(input('Segundo bimestre:'))

while b>10:
    b = int(input('Você digitou errado. Segundo bimestre:'))

c = int(input('Terceiro bimestre:'))

while c>10:
    c = int(input('Você digitou errado. Terceiro bimestre:'))

d = int(input('Quarto bimestre:'))

while d>10:
    d = int(input('Você digitou errado. Quarto bimestre:'))

media = (a+b+c+d)/4
# media = (3+5+8+9)/4

#imprime definindo quantas casas depois da virgula
print(f'Media: {media:10.2f}')

while True:
    parar=int(input('Digite 0 para sair:'))

    if parar == 0:
        break
    if parar == 5:
        continue
    print(parar)

