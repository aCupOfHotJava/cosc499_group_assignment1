# Implement snow feature for weather suggestion appplication
# @ Brandon Krieg

# driver will call snow function with ground conditions,
# precipitation chance, and wind speed. snow will return a list
# of wares that are recommended given the conditions

def snow(ground, precip, wind):
    wares = {}
    if(ground == "ice"):
        wares.append("Crampons", "Boots")
    elif(ground == "slush"):
        wares.append("Rubber boots")
    else:
        wares.append("Regular shoes")
    # TODO