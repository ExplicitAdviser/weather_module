import pyowm
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here

city = input('Какой город Вас интересует? : ')

owm = pyowm.OWM('ead19c96dd8e6cffc560ab3ee62f1199', config_dict)

mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
weather = observation.weather

temperature = weather.temperature('celsius')['temp']

print("В городе "+ city +" сейчас температура воздуха: " + str(temperature) + " по Цельсию. ")
print("В указанном городе " + weather.detailed_status)
