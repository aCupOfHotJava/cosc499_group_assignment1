# this is the driver file for all the separate features.
# feel free to use this to test your feature but it will
# be overwritten when we work on this file as a group
from snow import snow
from wind import wind
from rainy import bringUmbrella
from sunny import chancesOfSun

weather = input("Enter the expected weather: 'sunny', 'snow', 'rain', or 'wind': ")

if(weather == "snow"):
    ground = input("Enter the ground conditions: 'ice', 'slush', or other: ")
    precip = float(input("Enter the precipitation chance in [0.0, 1.0]: "))
    temperature0 = float(input("Enter the temperature in numeric form: "))
    snow(ground, precip, temperature0)
    
elif(weather == "wind"):
    airSpeed = float(input("Enter the airSpeed in Km/h: "))
    humidity = input("Is it humid in your area? ('yes/no'): ")
    wind(airSpeed, humidity)

elif(weather == "rain"):
    percentProbRain = float(input("Enter the percent chance of rain: "))
    isUmbrellaWeather = bringUmbrella(percentProbRain)
    if(isUmbrellaWeather):
        print("You should bring an umbrella")
    else:
        print("You probably don't need an umbrella")

elif(weather == "sunny"):
    temperature1 = float(input("Enter the temperature in numeric form: "))
    chancesOfSun(temperature1)