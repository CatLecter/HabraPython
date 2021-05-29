from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route("/")
def index():
    try:
        weather = weather_by_city("Moscow,Russia")
        if weather:
            return f"Погода сегодня {weather['temp_C']} градусов, ощущается как {weather['FeelsLikeC']}"
        else:
            return "Сервис погоды временно недоступен"
    except (requests.RequestException):
        print("Сетевая ошибка")


if __name__ == "__main__":
    app.run(debug=True)
