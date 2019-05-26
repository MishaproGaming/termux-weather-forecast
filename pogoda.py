import pyowm

owm = pyowm.OWM('66bfea7bff3208b9cbc01ec03f68ff7a',language = "ru")

mi = input ("В каком городе\стране вам надо узнать погоду?: ")

observation = owm.weather_at_place(mi)

w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print ( "В городе " + mi + " сейчас " + w.get_detailed_status())
print ( "Температура сейчас в районе " + str(temp))

if temp < 10:
     print ("Сейчас очень холодно,одевайся по теплее.")
elif temp < 20:
    print ("Сейчас холодно,оденься потеплее.")
else:
    print ("Температура нормальная,одевай что угодно.")
