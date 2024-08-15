import json
import requests
import sys

#Manejo de APIs

if len(sys.argv) != 2:
       sys.exit()

cantante = sys.argv[1]

#Busca cantante en iTunes
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term={cantante}" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
