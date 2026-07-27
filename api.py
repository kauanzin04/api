import requests

url = "https://wttr.in/Belo+Horizonte"

response = requests.get(url)
data = response.text

print(data)