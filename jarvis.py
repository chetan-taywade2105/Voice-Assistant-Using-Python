import pyttsx3 
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os 
import smtplib 
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id) to see voice options
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("good morning sir your buddy jarvis this side  tell me how  may i help you")

    elif hour>=12 and hour<18:
       speak("good afternoon sir your buddy jarvis this side tell me how  may i help you")
    else:
       speak("good evening sir your buddy jarvis this side tell me how  may i help you") 


def takeCommand():
    #takes microphone input and gives string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        #r.listen(source, timeout=3)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    prints error msg in o/p window
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('20010065@ycce.in', '')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()   

if __name__ == "__main__":
     wishMe()
     while True:
     #if 1:
    # loop for tasks if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'video' in query:
            music_dir = 'C:\\Users\\BHARGAV\\Videos\\DEMON SLAYER'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'Music' in query:
            music_dir = 'C:\\Users\\BHARGAV\\Videos\\DEMON SLAYER'
            songs = os.listdir(music_dir)
            print(songs)    
            random_song = random.choice(songs)
            print("Playing:", random_song)
            os.startfile(os.path.join(music_dir, random_song[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print("Sir, the time is ",{strTime})

        elif 'game' in query:
            codePath = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(codePath)

        elif 'who am i' in query:
            speak("sir you are my creator")
            print("sir you are my creator")

        elif 'group' in query:
            speak("My Creator group include Yashraj Tarte,Nikhil Talatule and Bhargav sable")
            print("My Creator group include Yashraj Tarte,Nikhil Talatule and Bhargav sable")
        
        else:
            speak("nothing heard")
