import pyttsx3   #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia    #pip install wikipedia
import webbrowser
import os, random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)  #0 for male and 1 for female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon!")

    else:
        speak("Good Eveninig!")

    speak(" I am Jarvis. Please tell me how may I help you")
    
    
def takeCommand():   #it takes microphone input from the user and returns string output               

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold = 800
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say this again please...")
        return "None"
    return query

def sendEmail(to, content):    #to send mail need allow less secure app from google
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rahulfrndz02@gmail.com', 'your-password-here')
    server.sendmail('rahulfrndz02@gmail.com', to , content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #logic for executing tasks based on query
       
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")       #wikipedia will replace with blank
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open mozila firefox' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'play music' in query:
            music_dir = 'M:\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[9]))
        
        # elif 'close music' in query:              #doubt
        #     music_dir = 'M:\\Songs'
        #     os.close(os.path(music_dir))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query:
              os.startfile('C:\\WINDOWS\\system32\\notepad.exe')

        # elif 'exit notepad' in query:
        #       exit('C:\\WINDOWS\\system32\\notepad.exe')
        
        elif 'open word' in query:
              os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

        elif 'open excel' in query:
              os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE')

        elif 'open power point' in query:
              os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE')
            
        
        elif 'open code' in query:
            os.startfile("C:\\Users\\Rahul Raj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            
 
        elif 'emial to rahul' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "rahulfrndz02@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend Rahul bro. I am unable to send this email")
    















