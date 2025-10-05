import os
import subprocess

# Definindo minhas constantes;
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Diretório base do script;
DIRECTORY = os.path.join(BASE_DIR, "../../")

print(DIRECTORY)

#subprocess.run(["rm", "teste.txt"])