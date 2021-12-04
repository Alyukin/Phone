import requests
domain = 'https://ipinfo.io/'
response = requests.get(domain).json()
print(response)