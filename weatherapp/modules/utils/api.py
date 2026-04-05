import requests

def get_data(city_name: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=2bf2e8aa6bbe3d941fc43499ab8e5306&units=metric&lang=ua")
    if response.status_code == 200:
        return response.json()

def get_weather(city_name: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=2bf2e8aa6bbe3d941fc43499ab8e5306&units=metric&lang=uk"
    api_key = "2bf2e8aa6bbe3d941fc43499ab8e5306"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=uk"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "temp": round(data['main']['temp']),
                "temp_min": round(data['main']['temp_min']),
                "temp_max": round(data['main']['temp_max']),
                "desc": data['weather'][0]['description'],
                "timezone": data['timezone'],
                "icon": data["weather"][0]["icon"],
                "coord": data["coord"]
            }
    except Exception as e:
        print(f"Помилка: {e}")
    return None

def get_forecast(lat: str, lon: str):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=2bf2e8aa6bbe3d941fc43499ab8e5306&units=metric&lang=uk"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Помилка: {e}")
    return None
