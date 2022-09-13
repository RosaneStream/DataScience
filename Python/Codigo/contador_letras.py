from json.tool import main


def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
      quantidade = len(x)
      contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'baleia']
    print(contador_letras(lista))

