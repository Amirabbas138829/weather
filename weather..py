import requests , json


api_key = "9adced7ddff5c6dc7f031455d3dec00e"
 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
 
response = requests.get(complete_url)

x = response.json()

a=x['main']['temp']
b=x['weather'][0]["main"]

print(city_name+" "+'is'+' '+b+' '+'and'+' '+str(a)+' '+'degrees.')