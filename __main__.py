# this is the driver file for all the separate features.
# feel free to use this to test your feature but it will
# be overwritten when we work on this file as a group
from snow import snow

weather = input("Enter the expected weather: 'sunny', 'snow', 'rain', or 'wind': ")
if(weather == "snow"):
    ground = input("Enter the ground conditions: 'ice', 'slush', or other: ")
    precip = float(input("Enter the precipitation chance in decimal form [0.0, 1.0]: "))
    temperature = float(input("Enter the temperature in numeric form: "))
    snow(ground, precip, temperature)