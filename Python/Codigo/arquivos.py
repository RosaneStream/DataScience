import shutil

#criar
def escrever_arquivo(caminho, texto):
    arquivo = open(caminho,'w')
    arquivo.write(texto)
    arquivo.close()

#atualizar
def atualizar_arquivo(caminho, texto):
    arquivo = open(caminho,'a')
    arquivo.write(texto)
    arquivo.close()

#ler
def ler_arquivo(caminho):
    arquivo = open(caminho,'r')
    texto = arquivo.read()
    arquivo.close()

def media_notas(caminho):
    arquivo = open(caminho,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)

    lista_media =[]
    for x in aluno_nota:
        lista_notas = x.split(',')
        #print(lista_notas)
        aluno = lista_notas[0]
        notas = lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas ])/4
        print(aluno)
        print(lista_notas)
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})

    return lista_media

#mover
def copia_arquivos(caminho):
    destino = 'C:/Users/rosan/Desktop/SBFD_DIO/notas.txt'
    shutil.copy(caminho, destino)

def move_arquivos(caminho):
    destino = 'C:/Users/rosan/Desktop/SBFD_DIO/'
    shutil.move(caminho, destino)

#abrir

#if __name__ == "main":
caminho = 'C:/Users/rosan/Desktop/SBFD_DIO/12_Python/notas.txt'
#copia_arquivos(caminho)
move_arquivos(caminho)

#texto = 'Maria, 9, 4, 8, 4 \n'
#atualizar_arquivo(caminho, texto)
#lista_media = media_notas(caminho)
#print(lista_media)