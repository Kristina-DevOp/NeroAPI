import requests

#response = requests.get('http://127.0.0.1:8000/drinks')
#print(response.json())

response = requests.get('https://api.spaceflightnewsapi.net/v3/articles')
print(response.json())

