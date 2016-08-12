import requests
url = 'https://api.weathersource.com/v1/{6b435fcc7129aeb69eef}/resource'
response = requests.get(url)
print response
