import requests
import json
r = requests.get(f"https://api.exchangeratesapi.io/latest?base=RUB&symbols=USD")
print(json.loads(r.content))