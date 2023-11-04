import requests
import os

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWN_API_KEY")


class Weather:
    def __init__(self, lat, long):
        self.weather_params = {
            "lat": lat,
            "lon": long,
            "appid": api_key
        }

    def get_weather_forecast(self):
        response = requests.get(OWN_Endpoint, params=self.weather_params)
        response.raise_for_status()
        weather_data = response.json()
        print(weather_data)

        current_weather = ""

        condition_code = weather_data["weather"][0]["id"]
        print(condition_code)
        if int(condition_code) < 600:
            current_weather = "It's going to rain today. Remember to bring an ☔️"
        elif 600 <= int(condition_code) < 700:
            current_weather = "It's going to snow today. Remember to wear a 🎩, 🧤, 🥾and 🧥"
        elif int(condition_code) == 800:
            current_weather = "It's going to clear today. It is a beautiful day☀️!"
        elif 801 <= int(condition_code) < 805:
            current_weather = "It's going to cloud today. Remember to wear an ☔️,  🥾 and 🧥"

        return current_weather

