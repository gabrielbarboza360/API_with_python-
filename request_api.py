
import requests

#fazendo Requisição na API que desenvolvi separadamente em outro arquivo
url = 'http://localhost:5000/lista'
response = requests.get(url)

def get_user():
    data = response.json()
    frases_atualizadas = []
#Depois de realizar a requisição, faço uma atualização de uma variavel vazia dentro da API, enviando por metodo PUT
    for cliente in data:
        cliente['frase'] = 'inserindo uma frase dentro da variavel vazia na API'
        frases_atualizadas.append(cliente)

    update_response = requests.put(url, json=frases_atualizadas)

    if update_response.status_code == 200:
        print('Frases atualizadas com sucesso.')
    else:
        print('Falha ao atualizar as frases. Código de status:', update_response.status_code)

get_user()
