import requests

def get_weather(city, api_key):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    print(f"Weather in {city}: {weather}, Temperature: {temp}°C")
  else:
    print(f"Failed to get weather for {city}. Status code: {response.status_code}")

if __name__ == "__main__":
  # Replace with your OpenWeatherMap API key
  API_KEY = "YOUR_API_KEY"
  city = input("Enter city name: ")
  get_weather(city, API_KEY)