# Weather Information Fetcher

This Python script fetches and displays weather information for a specified city using the OpenWeatherMap API.

## Features

- Send a GET request to the weather API with the city name.
- Extract temperature, humidity, and weather description from the JSON response.
- Display the weather information in a readable format.
- Handle network issues and invalid API responses gracefully.

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/weather-fetcher.git
    cd weather-fetcher
    ```

2. Install the required libraries:
    ```sh
    pip install requests
    ```

## Usage

1. Enter your API key in the script:
   Replace `"your_api_key_here"` with your actual OpenWeatherMap API key in the `fetch_weather_data` function.

2. Run the script:
    ```sh
    python weather_fetcher.py
    ```

3. Enter the city name when prompted:
    ```sh
    Enter city name: London
    ```

## Script Details

### fetch_weather_data(api_url, city_name, api_key)

Sends a GET request to the OpenWeatherMap API and retrieves weather data for the specified city.

**Parameters:**
- `api_url`: Base URL of the OpenWeatherMap API.
- `city_name`: Name of the city to fetch weather data for.
- `api_key`: Your OpenWeatherMap API key.

**Returns:**
- A dictionary containing temperature, humidity, and weather description if the city is found.
- `None` if the city is not found or if there is a network issue or API response error.

### display_weather(data)

Displays the weather information in a readable format.

**Parameters:**
- `data`: Dictionary containing weather information.

**Returns:**
- None

## Example Output

```sh
Enter city name: Lahore
Temperature: 36.99°C
Humidity: 47%
Weather Description: haze
```
