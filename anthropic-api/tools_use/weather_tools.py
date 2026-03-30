import os
import json
import requests
from dotenv import load_dotenv
from anthropic.types import ToolParam
load_dotenv()


def get_weather(location):
    if not location or location.strip() == "":
        raise ValueError("Location cannot be empty.")
    weather_api_key = os.getenv("WEATHER_API_KEY")
    api_request_url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={location}"
    response = requests.get(api_request_url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return {
        "location": data["location"]["name"],
        "country": data["location"]["country"],
        "temp_c": data["current"]["temp_c"],
        "temp_f": data["current"]["temp_f"],
        "condition": data["current"]["condition"]["text"],
        "humidity": data["current"]["humidity"],
        "wind_kph": data["current"]["wind_kph"],
    }


get_weather_schema = ToolParam({
    "name": "get_weather",
    "description": "Gets the current weather for a given location using the WeatherAPI service.",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city or location to get weather for, e.g. 'London' or 'New York'.",
            }
        },
        "required": ["location"],
    },
})
