#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


def ZA(P,T,H):
    Pf = P*(1-((0.0065*H)/(T+0.0065*H+273.15)))
    Pfinal=math.pow(Pf,-5.27)                           

    Z=0.0
    if(Pfinal>P):
        print("Pressure is rising")
        Z=179-((2*Pfinal)/129)
        
    elif(Pfinal<P):
        print("Pressure is falling")
        Z=130-(Pfinal/81)
    else:
        Z=147-(5*Pfinal/376)
        
    if(H==1):
        print("Adjustment of value of Z based on Wind Direction")
        print("1. Northerly Winds")
        Z=Z+1
    elif(H==2):
        print("Adjustment of value of Z based on Wind Direction")
        print("2.Southerly Winds")
        Z=Z-2
    else:
        print("Wrong choice")
        
        
        
        
    if(T==1):
        print("Adjustment For Season")
        print("1..Winter")
        Z=Z-1
    elif(T==2):
        print("2..Summer")
        Z=Z+1

    if(Z>32):
            Z=Z%32
    if(Z==1):
        print("Settled Fine")
    elif(Z==2):
        print("Fine Weather")
    elif(Z==3):
         print("Fine Becoming Less Setled")
    elif(Z==4):
        print("Fairly fine Showery Later")
    elif(Z==5):
        print("Showering Becoming More unsettled")
    elif(Z==6):
        print("Unsettled, Rain Later")
    elif(Z==7):
        print("Rain at times, Worse Later")
    elif(Z==8):
        print("Rain at times ,Becoming Very unsettled")
    elif(Z==9):
        print("Very Unsettled, Rain")
    elif(Z==10):
        print("Settled Fine")
    elif(Z==11):
        print("Fine Weather")
    elif(Z==12):
        print("Fine,Possibly Showers")
    elif(Z==13):
        print("Fairly Fine, Showers Likely")
    elif(Z==14):
        print("Showery,Bright Intervals")
    elif(Z==15):
        print("Changeble,Some Rain")
    elif(Z==16):
        print("Unsettled, Rain at times")
    elif(Z==17):
        print("Rain at frequent Intervals")
    elif(Z==18):
        print("Very Unsettled,Rain")
    elif(Z==19):
        print("Stormy, Much Rain")
    elif(Z==20):
        print("Settled,Fine")
    elif(Z==21):
        print("Fine Weather")
    elif(Z==22):
        print("Becoming Fine")
    elif(Z==23):
        print("Fairly Fine, Improving")
    elif(Z==24):
        print("Fairly Fine, Possibly Showers early")
    elif(Z==25):
        print("Showery Early,Improving")
    elif(Z==26):
        print("Changeble,Mending")
    elif(Z==27):
        print("Rather Unsettled, Clearing Later")
    elif(Z==28):
        print("Unsettled,Probably Improving")
    elif(Z==29):
        print("Unsettled, Short Fine Intervals")
    elif(Z==30):
        print("Very Unsetttled, Finer At Times")
    elif(Z==31):
        print("Stormy, Possibly Improving")
    elif(Z==32):
        print("Stormy, Much Rain")
    else:
        print("Unsettled,Changeble")
    return
    
P=float(input("Enter you measured pressure"))
T=float(input("Enter your measured Temperature in Celcius"))
H=float(input("enter your altitude in meters"))
ans=ZA(P,T,H)


    


# In[ ]:




