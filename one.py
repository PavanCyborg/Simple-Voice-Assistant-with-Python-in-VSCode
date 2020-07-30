import pyttsx3
import os
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import smtplib
import encyclopedia

print('INITIALIZING  JARVIS.....')
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
print(voices)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def timedate():
    time=int(datetime.datetime.now().hour)
    print(time)

    if time>=00 and time<12:
        speak("good morning sir")
    elif time>=12 and time<=15:
        speak("good afternoon sir") 
    elif time>15 and time<=19:
        speak("good evening sir")
    else :
        speak('good night sir')                   


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening:....")
        audio= r.listen(source)

    try:
        print("recogninzing......") 
        #query=r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY") 
        query= r.recognize_google(audio,language= 'en-in')
        print(f"user said: {query} \n")
    except Exception as e:
        speak("sorry unable to hear you")   
        print("unable to hear you")
        query= None
    return query    

speak("initializing jarvis")
query=takecommand()

#logic for executing basic tasks....


if 'wikipedia' in query:
    speak("Searching wikipedia....")
    print("Searching WIKIPEDIA")
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=3)
    print(results)
    speak(results)
            
elif 'open youtube' in query.lower():
    print("opening youtube")
    speak("opening youtube....")
    webbrowser.open("youtube.com")
            
elif 'music' in query:
    songdir="D:\\songs"
    songs=os.listdir(songdir) 
    print(songs)
    os.startfile(os.path.join(songdir,songs[0]))       
elif 'the time' in query:
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    print(strTime)
    speak(f"sir the time is {strTime}... ")
            
elif 'open code' in query.lower():
    code="C:\\Users\\PAVAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\code.exe"
    print('opening VS code')
    speak("opening Visual studio code...")
    os.startfile(code)
            
elif 'send mail' in query.lower():
    try:
        speak('ok sir what should i send as an email...')
        content=takecommand()
        to="kvsaigopal3@gmail.com"  
        email(to,content)
        print('email sent')
        speak("email has been sent successfully...")
    except Exception as e:
        print(e)      
elif 'tell me about' in query:
    speak("SEARCHING ENCYCLOPEDIA....")
    print("searching encyclopedia")
    queryx=query.replace("encyclopedia","")
    result=encyclopedia(queryx)
    print(result)
    speak(result)


def email(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() 
    server.starttls()
    server.login('pavankasina99@gmail.com','9849928447')
    server.sendmail('kvsaigopal3@gmail.com',to,content)
    server.close()
