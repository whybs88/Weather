# Name: Jeremy Weible
# Date: 7/30/2023
import json
import requests

def get_weather_data(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    appid = "ea2e428502a995b71d53efd6140f4937"

    url = f"{base_url}?q={city}&units=imperial&APPID={appid}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            unformatted_data = response.json()

            temp = unformatted_data["main"]["temp"]
            temp_max = unformatted_data["main"]["temp_max"]
            weather_desc = unformatted_data["weather"][0]["description"]

            print(f"\nWeather forecast for {city.capitalize()}:")
            print(f"Temperature: {temp}°F")
            print(f"Max Temperature: {temp_max}°F")
            print(f"Description: {weather_desc.capitalize()}")
        else:
            print("Error: Unable to fetch weather data. Please try again later.")
    except requests.exceptions.RequestException as e:
        print("Error: Connection to the weather service failed. Please check your internet connection.")
    except json.JSONDecodeError as e:
        print("Error: Failed to decode weather data. Please try again later.")

def main():
    while True:
        print("\nWelcome to Weather Forecast Application!")
        city = input("Please enter a city name or zip code (type 'exit' to quit): ")

        if city.lower() == "exit":
            print("Exiting the application. Goodbye!")
            break

        if city.strip():
            get_weather_data(city)
        else:
            print("Error: Please enter a valid city name or zip code.")

if __name__ == "__main__":
    main()
