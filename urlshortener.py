#This app will shorten any url we need to install the module pyshortener

import pyshorteners
url=input("Enter the url:")  #ask for the url
shortener=pyshorteners.Shortener()  #stores the method
a=shortener.tinyurl.short(url)  #shortens the url
print(a) #prints the url