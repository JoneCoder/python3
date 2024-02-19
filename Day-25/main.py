import requests

url = "https://www.w3schools.com/"

response = requests.get(url)

print(response.text)