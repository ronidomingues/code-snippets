import os
import requests

# Definindo minhas constantes;
USER = "ronidomingues" # Usuario do GitHub;
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Diretório base do script;
OUTPUT_FILE = os.path.join(BASE_DIR, "repositories.txt") # Arquivo de saída;

# Faz a requisição para a API do GitHub afim de obter os repositórios do usuário;
response = requests.get(f"https://api.github.com/users/{USER}/repos")
response.raise_for_status() # Levanta um erro se a requisição falhar;
response = response.json() # Converte a resposta para JSON;

# Escreve os nomes dos repositórios no arquivo de saída;
with open(OUTPUT_FILE, "a") as file:
    for repo in response:
        file.write(USER + '/' + repo['name'] + "\n")