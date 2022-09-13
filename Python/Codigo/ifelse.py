
# a = int(input('Primeiro bimestre:'))

# if a>10:
#     a = int(input('Você digitou errado. Primeiro bimestre:'))

# b = int(input('Segundo bimestre:'))

# if b>10:
#     b = int(input('Você digitou errado. Segundo bimestre:'))

# c = int(input('Terceiro bimestre:'))

# if c>10:
#     c = int(input('Você digitou errado. Terceiro bimestre:'))

# d = int(input('Quarto bimestre:'))

# if d>10:
#     d = int(input('Você digitou errado. Quarto bimestre:'))

# media = (a+b+c+d)/4
media = (3+5+8+9)/4

a = 3

b = 5

c= 8

d = 9

if c % 2 == 0:
    print('C={} é par'.format(c))

if not a % 2 == 0:
    print('A={} nao é par'.format(a))

if a>b and a>c and a>d:
    print('A={} é a maior nota'.format(a))
elif b>a and b>c and b>d:
    print('B={} é a maior nota'.format(b))
elif c>a and c>b and c>d:
    print('C={} é a maior nota'.format(c))
else: print('D={} é a maior nota',d)

print('Media: {}',media)

status = "Aprovado" if media>=7 else "Reprovado"
print(f'Situacao: {status}')