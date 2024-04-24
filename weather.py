import requests, json
api ="a6d2c1769c798398e2de61bb43d0dc39"
url="https://api.openweathermap.org/data/2.5/weather?lat=21.0285&lon=105.8352&appid="
city=input()
competeurl= url+api
reponse=requests.get(competeurl)
data=reponse.json()['weather'][0]['main']
print(data)


