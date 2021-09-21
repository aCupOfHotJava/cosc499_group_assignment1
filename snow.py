# Implement snow feature for weather suggestion appplication
# @ Brandon Krieg

# driver will call snow function with ground conditions,
# precipitation chance, and wind speed. snow will return a list
# of wares that are recommended given the conditions

# no exception handling or input checks, just a quick program
# for the group assignment

def snow(ground, precip, temperature):
    wares = []
    if(ground == "ice"):
        wares.append("Crampons")
        wares.append("Boots")
    elif(ground == "slush"):
        wares.append("Rubber boots")
    else:
        wares.append("Regular shoes")
    if(precip > 0.5):
        wares.append("Hood")
    if(temperature < 0):
        wares.append("Heavy jacket")
    else:
        wares.append("Light jacket")
    print("You should wear: ")
    print(*wares, sep = ", ")