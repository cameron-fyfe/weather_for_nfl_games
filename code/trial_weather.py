# Import the required libraries
from pyowm.owm import OWM
from pyowm.utils import timestamps

# Set the API key for OpenWeatherMap
api_key = 'input_API_key_here_please'

# Create an instance of the OWM client
owm = OWM(api_key)

# Weather manager
mgr = owm.weather_manager()

# Get the projected weather for a particular city
city = 'London'
daily_forecast = mgr.forecast_at_place(city, 'daily').forecast
print("The daily forecast is: ", daily_forecast)

# Tomorrow's weather
tomorrow = timestamps.tomorrow()

# Get the projected temperature in a city
temperature = daily_forecast.get_temperature(unit='celsius')
print(f'The projected temperature in {city} is {temperature} degrees Celsius.')

# Get the projected weather conditions in a city
weather = daily_forecast.get_weather(tomorrow)
print(f'The projected weather conditions in {city} tomorrow are: {weather}.')