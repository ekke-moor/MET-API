```python
import requests

# API endpoint and API key
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "YOUR_API_KEY"
lat = 38.7267
lon = -9.1403

# API parameters
params = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key,
    "units": "metric"
}

# Make the API request
response = requests.get(api_endpoint, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract and iterate through the next 3 hours forecast
    for hour in data["hourly"][:3]:
        temperature = hour["temp"]
        time = hour["dt"]
        weather_icon = hour["weather"][0]["icon"]
        
        print(f"Time: {time}, Temperature: {temperature}°C, Weather Icon: {weather_icon}")
else:
    print("Error fetching weather data.")

```
