import requests

baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'q': 'Memphis,US',
    'appid': '792d505e7a9c3b263140201a5658b4fc',
}

response = requests.get(baseUrl, params=parameters)
print(response.content)
