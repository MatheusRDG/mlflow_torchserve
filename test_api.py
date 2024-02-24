import requests

# URL do endpoint Flask
url = 'http://localhost:8080/api'

# Dados para enviar na solicitação (em formato JSON)
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# Faz a solicitação POST para o endpoint Flask
response = requests.post(url, json=data)

# Verifica se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Exibe a resposta do servidor
    print('Resposta do servidor:', response.json())
else:
    # Se a solicitação não foi bem-sucedida, exibe o status do erro
    print('Erro:', response.status_code)