import requests

url = "https://wttr.in/Carapicuiba"

response = requests.get(url)
data = response.text

print(data)