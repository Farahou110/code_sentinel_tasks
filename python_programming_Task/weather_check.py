import requests
import os
import json
from os import getenv
from dotenv import load_dotenv

load_dotenv()  

def get_weather_data():
    # API configuration
    API_KEY = ("72251afad3a71c189758e40bd2788092")  #os.getenv("OPEN_WEATHER_API_KEY")  
   
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    city = input("Enter the city name: ").strip()
    
    if not city:
        print("City name cannot be empty!")
        return
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  
    }
    
    try:
        # Make API request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  
        
        # Parse JSON response
        data = response.json()
        
        # Extract relevant information
        if data['cod'] == 200:  # Successful response
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            conditions = data['weather'][0]['description']
            
            # Display the weather information
            print("\n" + "*_"*20)
            print(f"Weather in {city.title()}:")
            print("_*"*20)
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {conditions.title()}")
            print("="*40)
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except json.JSONDecodeError:
        print("Error parsing response from server")
    except KeyError as e:
        print(f"Unexpected response format: Missing key {e}")

if __name__ == "__main__":
    get_weather_data()