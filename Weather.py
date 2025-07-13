import requests
import re
API_KEY = "eb95f1f871e178d96d907941821bbd9e"
CITY="Boryslav"
URL = "http://api.openweathermap.org/data/2.5/weather?q=Boryslav&appid=eb95f1f871e178d96d907941821bbd9e&units=metric&lang=ua"


respinse = requests.get(URL)
data = respinse.json()
def format_weather(data):
    temp = data["main"]["temp"]

    description=data["weather"][0]["description"]

    humidity =data["main"]["humidity"]

    wind =data["wind"]["speed"]

    report  = (
        f"Температура: {temp}градусів Цельсія.\n"
        f"Опис: {description}\n"
        f"Вологість: {humidity}%.\n"
        f"Вітер: {wind}  метрів за секунду"
    )
    return report
def  replace_decimal_point(text):
    return re.sub(r'(?<=\d)\.(?=\d)', ' крапка ', text)

