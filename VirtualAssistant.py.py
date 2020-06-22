import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import time
from time import ctime
import re
import webbrowser
import smtplib
import bs4
import requests


def listen():
    r = sr.Recognizer()
    with sr.Microphone () as source:
        print(" I am listening..")
        audio = r.listen(source,phrase_time_limit = 5)
    data=""
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear/understand you")
    except sr.RequstError as e:
        print("Request Failed")
    return data

def respond (String):
    print(String)
    tts = gTTS(text=String, lang="en")
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")

def voice_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I am well, thank you")
    if "time" in data:
       listening = True
       respond(ctime())
    if "date" in data:
        listening = True
        respond(ctime())
    if "what is your name" in data:
        listening = True
        respond("My name is Cortana")
        
    if "open Google" in data: #Converts uppercase or lowercase letter     
       listening = True
       reg_ex = re.search("open Google(.*)",data)
       url = "https://www.google.com"
       if reg_ex:
           subgoogle = reg_ex.group(1)
           url = url
       webbrowser.open(url)
       respond("Done Sir")

    if "email" in data:
        listening =True
        respond("Sir, whom shall I send an e-mail to?")
        to = listen()

        edict = {"just":"your email","real":"friend's email"}
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("Sir what should I tell that person?")
        message = listen()
        content = "subject : {}\n\n{}".format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP("smtp.gmail.com",587)

        #identify the server
        mail.ehlo()
                            
        mail.starttls()

        #login
        mail.login("your email","your password")
                 
        mail.close()

        respond("Sir, e-mail sent")

        if "Wikipedia" in data.casefold():
         


         listening = True
         respond("Sir, whgat should I search?")
         query = listen()
         response = requests.get("https//en.wikipedia.org/wiki/" +query)
         if response is not None:
             html = bs4.BeautifulSoup(response.text,"html.parser")
             paragraphs = html.select("p")
             intro = "".join(intro)
             respond(halo[:200])

        if "stop" in data:
             listening = False
             print("Listening Stopped")
             respond("See you Sir")
          
                 
                 


       
time.sleep(1)
respond("Hello Sir,what can I do for you?")
listening = True
while listening == True:
    data = listen() #call the listen() here
    listening = voice_assistant(data)   
    
