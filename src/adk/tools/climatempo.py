import requests


def get_lat_long(cidade: str) -> tuple[float, float]:
    """
    Get the latitude and longitude of a city
    Args:
        cidade: The city to get the latitude and longitude of
    Returns:
        A tuple of the latitude and longitude of the city
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=10&language=en&format=json"
    response = requests.get(url)
    data = response.json()
    return data['results'][0]['latitude'], data['results'][0]['longitude']


def get_forecast(cidade: str) -> dict:
    """
    Get the forecast for a city
    Args:
        cidade: The city to get the forecast of
    Returns:
        A dictionary of the forecast for the city
    """
    latitude, longitude = get_lat_long(cidade)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_lat_long("Dourados"))
    print(get_forecast("Dourados"))