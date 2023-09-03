import requests
import environ
import openai
from config.settings.base import BASE_DIR

env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))


def call_weather_api(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={env('API_KEY')}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()

        # Extract weather data in a more readable way
        weather_details = weather_data['weather'][0]
        main_details = weather_data['main']
        wind_details = weather_data['wind']
        sys_details = weather_data["sys"]

        weather_info = {
            "city_name": weather_data['name'],
            "weather_main": weather_details['main'],
            "temperature": round(main_details['temp']),
            "humidity": main_details['humidity'],
            "wind_speed": round(wind_details['speed'], 1),
            "weather_icon": weather_details['icon'],
            "country": sys_details["country"]
        }
        return weather_info
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def get_clothing_recommendation(weather_data):
    openai.api_key = env('OPENAI_KEY')

    prompt = f"""Given the weather data: {weather_data}, recommend suitable clothing in the following form (3 categories):
    Clothing: maximum 5 elements of suitable clothing
    Shoes: maximum 5 elements of suitable clothing
    Accessories: maximum 3 elements of suitable accessories
    """

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        split_text = response.choices[0].text.split("\n")

        return {"clothing": split_text[1][10:],
                "shoes": split_text[2][7:],
                "accessories": split_text[3][13:]}

    except Exception as e:
        print(f"Error generating clothing recommendation: {e}")
        return None
