import requests

api_key = '9e3c5085d95648026083f1649a21ec1e'

city_name = "jakarta"

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
print(url)

req = requests.get(url)
data = req.json()

name = data['name']
lon = data['coord']['lon']
lat = data['coord']['lat']

print(name, lon, lat)

exclude = "hourly"

url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}'
print(url2)

req2 = requests.get(url2)
data2 = req2.json()
print(data2)

days = []
nights = []
descr = []

for i in data2['daily']:

    days.append(round(i['temp']['day'] - 273.15, 2))

    nights.append(round(i['temp']['night'] - 273.15, 2))

    descr.append(i['weather'][0]['main'] + ": " + i['weather'][0]['description'])

string = f'[ {name} - 8 days forecast]\n'

for i in range(len(days)):

    if i == 0:
        string += f'\nDay {i + 1} (Today)\n'

    elif i == 1:
        string += f'\nDay {i + 1} (Tomorrow)\n'

    else:
        string += f'\nDay {i + 1}\n'

    string += 'Morning:' + str(days[i]) + '°C' + "\n"
    string += 'Night:' + str(nights[i]) + '°C' + "\n"

print(string)