import requests
import json
import pyttsx3

city = input("Enter the name of the city:\n")

url = f"https://api.weatherapi.com/v1/current.json?key=4d71526ed31c4b0ebaf105756241105&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
engine = pyttsx3.init()
engine.say(f"The current weather in {city} is {w} degrees Celsius")
engine.runAndWait()















# import requests
# import json
# import os
#
# city = input("Enter the name of the city:\n")
#
# url = f"https://api.weatherapi.com/v1/current.json?key=4d71526ed31c4b0ebaf105756241105&q={city}"
#
# r = requests.get(url)
# print(r.text)
# wdic = json.loads(r.text)
# w = wdic["current"]["temp_c"]
#
# os.system(f"say 'the current weather in {city} is {w} degrees")



