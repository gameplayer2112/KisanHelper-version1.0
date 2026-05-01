import requests
import intro
import os
from dotenv import load_dotenv
load_dotenv()
my_key=os.getenv('weather_key')
def weather(name):
    intro.introduce(name)
    city=input('enter your city:')
    myapi=my_key
    url=f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={myapi}&units=metric'
    response=requests.get(url)
    forecast=response.json()
    for data in forecast['list']:
        if '12:00:00' in data['dt_txt']:
            date=data['dt_txt']
            temp=data['main']['temp']
            humidity=data['main']['humidity']
            weather=data['weather'][0]['description']
            wind=data['wind']['speed']
            print(f'the weather details for {city} on {date} are:')
            print(f'temperature:{temp}\u00b0 celsius')
            print(f'weather:{weather}')
            print(f'humidity:{humidity}%')
            print(f'wind speed:{wind}m/s')
        # {"main":{"temp":28.5,"humidity":65},"weather":[{"description":"clear sky"}]}
        # above example as reference
            [print('-',end='') for x in range(0,29)]
            print('\n')
if __name__=='__main__':
    name=input('enter your name:')
    weather(name)
