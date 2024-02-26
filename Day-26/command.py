import sys
import requests

arguments = sys.argv

url = arguments[1]
fileName = arguments[2]

content = requests.get(url).content

with open(fileName, 'wb') as f:
    f.write(content)
