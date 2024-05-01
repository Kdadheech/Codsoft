import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good evening")
    else:
        speak("good night")

    speak("hello i am jarvis please tell me how may i help you")

def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio,Language='en-in')
        print("USER SAID:",query)
    except Exception as e:

        print("say that again please...")
        return "None"
    return query 



if __name__=="__main__":
    wishMe()
    while True:
        query=takecmd().lower()



        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        
        elif 'open google' in query:
            webbrowser.open("google.com")

         
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"sir the time is:{strTime}")

        elif 'open code' in query:
            code="C:\\Users\\kanak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)   
             
        elif 'send email to my friend' in query:
            try:
                speak("what should i say")
                content=takecmd()
                to="kanak.dadheech@gmail.com"
                sendEmail(to,content)
                speak('Email has been sent!!')
            except Exception as e:
                print(e)
                speak("Sorry i am unable to send email at the moment")
