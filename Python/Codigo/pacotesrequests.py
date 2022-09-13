#install pip request
import requests

def retorna_dadoscep(cep):
    # solicitando acesso a uma pagina com o get
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    # code 200 é sucesso , 400 não encontrado
    print(response.status_code)
    # imprime o conteudo da pagina em forma de texto
    print(response.text)
    dados_cep = response.json()
    # imprime o conteudo da pagina no formato json - tipo dict (dicionario)
    print(dados_cep)
    # imprime somente uma informaçao do conteudo do dicionario
    print(dados_cep['logradouro'])
    return dados_cep

def retorna_dadospokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    # code 200 é sucesso , 400 não encontrado
    print(response.status_code)
    # imprime o conteudo da pagina em forma de texto
    print(response.text)
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_dadosurl(url):
    response = requests.get(url)
    # code 200 é sucesso , 400 não encontrado
    print(response.status_code)
    # imprime o conteudo da pagina em forma de texto
    return response.text


if __name__ == '__main__':
    #cep = retorna_dadoscep('80060000')
   # poke = retorna_dadospokemon('pikachu')
    # imprime o conteudo da pagina no formato json - tipo dict (dicionario)
    #print(poke)
    # imprime somente uma informaçao do conteudo do dicionario
    #print(poke['sprites']['front_female'])

    response = retorna_dadosurl('https://github.com/')
    print(response)