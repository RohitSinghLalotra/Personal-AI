import requests

def get_weather(location=""):
    """Get weather using wttr.in service"""
    url = f"http://wttr.in/{location}?format=j1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        
        current = data['current_condition'][0]
        area = data['nearest_area'][0]
        
        print(f"\nWeather for {area['areaName'][0]['value']}, {area['country'][0]['value']}")
        print(f"Temperature: {current['temp_C']}°C - {current['weatherDesc'][0]['value']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind: {current['windspeedKmph']} km/h")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    location = input("Enter location: ") or ""
    get_weather(location)
