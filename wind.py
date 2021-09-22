# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:32:54 2021

@author: alphi
"""

def wind(airSpeed, humidity):
    
    if(airSpeed >90 ):
        print("there is a wind warning in your area")
    elif(airSpeed <=90 and airSpeed >10):
        print("it will be windy in your area")
    if(humidity == "yes"):
        print("you might also experience rain or a hurricane warning")
    elif(humidity=="no"):
        print("you might be in a middle of a heatwave")