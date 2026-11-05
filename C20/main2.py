import requests

url = "https://en.wikipedia.org/api/rest_v1/page/summary/Artificial_intelligence"
res = requests.get(url)

data = res.json()
print(data["extract"])