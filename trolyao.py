#noi
import speech_recognition
import pyttsx3
import requests, json
from datetime import date,datetime
robotmouth= pyttsx3.init()
robotbrain=""
while True:
    robotear=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("robot: I'm listening")
        audio= robotear.listen(mic)
    print("Robot:...")
    try:    
        you=robotear.recognize_google(audio)
    except:
        you=""
    print("you: " + you)    
    #hieu
    if you =="hello":
        robotbrain="hello Mr Thắng"
    elif "your name" in you:
        robotbrain="my name is Tulen"
    elif "your mission" in you:
        robotbrain="answer your question"
    elif "boss" in you:
        robotbrain=" you are my master"
    elif "president" in you:
        robotbrain="Joe Biden"
    elif "today" in you:
        today=date.today()
        robotbrain = today.strftime("%B %d, %Y")
    elif "bye" in you:
        robotbrain="Bye Mr Thang"
        print(robotbrain)
        robotmouth.say(robotbrain)
        robotmouth.runAndWait()
        break
    elif "weather" in you:
        api ="a6d2c1769c798398e2de61bb43d0dc39"
        url="https://api.openweathermap.org/data/2.5/weather?lat=21.0285&lon=105.8352&appid="
        competeurl= url+api
        reponse=requests.get(competeurl)
        robotbrain=reponse.json()['weather'][0]['main']
    elif "time" in you:
        now=datetime.now()
        robotbrain = now.strftime("%H hour %M minute %S second")    
    elif you =="":
        robotbrain="I can't understand"
    else:
        robotbrain="Ï'm fine thanks"    
    print(robotbrain)
    #nghe
    robotmouth.say(robotbrain)
    robotmouth.runAndWait()
    