import requests  # pip install requests
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

city_name = input('please fill up your city ')

api_key = 'd82759ebf4a4a5ed987117c4027b9dfa'  # if api_key not works, generate yours on website

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
r_data = response.json()
if r_data["cod"] != "404":
    y = r_data['main']
    current_t = y['temp']
    current_p = y["pressure"]
    z = r_data["weather"]
    weather_description = z[0]["description"]
    print(str((round(current_t - 273.15))), str(current_p))
else:
    print('city not found')

"""
1. создать функцию(ии) для  определения погоды по данным(Город).
2. Вынести некоторые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать модуль test_wheather.py  внутри создать Класс для тестирования функции, с помощью unittest.
mock, patch
"""
