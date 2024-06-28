import requests

def fetch_weather_data(api_url, city_name, api_key):
    try:
        # Construct the complete URL
        complete_url = f"{api_url}appid={api_key}&q={city_name}&units=metric"
        
        # Send GET request to the weather API
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        # Extract data from the JSON response
        weather_data = response.json()

        if weather_data["cod"] != "404":
            main = weather_data["main"]
            weather = weather_data["weather"][0]
            
            return {
                'temperature': main['temp'],
                'humidity': main['humidity'],
                'weather_description': weather['description']
            }
        else:
            print("City Not Found")
            return None

    except requests.RequestException as e:
        # Handle network issues
        print(f"Network error occurred: {e}")
        return None
    except (KeyError, IndexError) as e:
        # Handle issues with the API response structure
        print(f"Error processing API response: {e}")
        return None

def display_weather(data):
    if data:
        print(f"Temperature: {data['temperature']}°C")
        print(f"Humidity: {data['humidity']}%")
        print(f"Weather Description: {data['weather_description']}")
    else:
        print("No weather data available")

# Example usage
if __name__ == "__main__":
    # Enter your API key here
    api_key = "1517ed8b6e93dae5197a90c3e4754de1"

    # Base URL to store the weather API endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = input("Enter city name: ")
    
    # Fetch and display weather data
    weather_data = fetch_weather_data(base_url, city_name, api_key)
    display_weather(weather_data)
