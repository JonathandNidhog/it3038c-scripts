import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=8562c8f6784883068a3a424f16784aa0' % zip)
data=r.json()
print(data['weather'][0]['description'])