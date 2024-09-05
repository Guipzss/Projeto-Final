import requests
import json

jogos = requests.get("http://localhost:5000/jogos")
jogos = jogos.json()
print(jogos)