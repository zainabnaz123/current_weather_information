import requests
import os

from datetime import datetime 
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv()

user_apikey= os.environ['current_weather_data']
location =input("Enter your city name :")

complete_API_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_apikey
api_link=requests.get(complete_API_link)
api_data = api_link.json()
print(api_data) 
if api_data['cod']== '404':
    print("INvalid city :{},please check your city name ".format(location))
else :
    temp_city=((api_data['main']['temp'] )-273.15)
    weather_desc= api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time= datetime.now().strftime("%d %b %Y |%I: %M: %S: %p")
    
    print("--------------------------------------------") 
    print("Weather State for -{} ||{}".format(location.upper(),datetime))   
    print("--------------------------------------------") 
    
    print("Current temperature is :{:.2f}deg C".format(temp_city))
    print("Current weather desc :",weather_desc)
    print("Current humidity:",hmdt,'%')
    print("Current wind speed:",wind_spd,'kmph')
    
    
    
    
