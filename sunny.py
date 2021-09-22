# going to implement a feature for sunny weather - Sophia

#function to print statements on if it will be sunny or not based on the weather (in degrees Celsius)
def chancesOfSun(weather):
    if weather < 15:
        print("It will most likely not be sunny today")
    elif weather > 16 and weather < 20:
        print("It may be sunny today")
    else:
        print("There is a high chance it will be sunny today!") 

#chancesOfSun(14)
 