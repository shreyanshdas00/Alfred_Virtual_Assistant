#%%
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
#import webbrowser
import os
import smtplib
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Alfred at your service sir. How may i assist you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)    
        print("Say that again please...")
        speak("I was unable to hear you.")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if(query=="none"):
            continue
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            #webbrowser.open("youtube.com")
            speak('On it')
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://youtube.com')
            

        elif 'open google' in query:
            #webbrowser.open("google.com")
            speak('On it')
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://google.com')
            
        elif ('search' in query and 'on google' in query) or 'on google' in query:
            speak('On it')
            query = query.replace("search", "")
            query = query.replace("on google", "")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://google.com')
            searchbox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
            searchbox.send_keys(query)
            searchbutton=driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')
            searchbutton.submit()
            
        elif ('search' in query and 'on youtube' in query) or 'on youtube' in query:
            speak('On it')
            query = query.replace("search", "")
            query = query.replace("on youtube", "")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://youtube.com')
            searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
            searchbox.send_keys(query)
            searchbutton=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
            searchbutton.click()


        elif 'open stackoverflow' in query:
            #webbrowser.open("stackoverflow.com")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://stackoverflow.com')


        elif 'play music' in query:
            music_dir = 'path/to/songs/directory'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open app' in query:
            codePath = "'path/to/songs/app"
            os.startfile(codePath)

        elif 'email to receiver' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")  
                
        elif 'how are you' in query:
            speak("I am good sir, thanks for asking. Hope you're doing well too?")
            
        elif 'hi' in query or 'hello' in query:
            speak("Hello sir, how can i be of service?")
            
        elif 'a joke' in query:
            speak("As you wish")
            speak("When is the best time to go to the dentist?")
            print("When is the best time to go to the dentist?")
            speak("at toothh:hurty!!")
            print("At tooth-hurty!!!\n\n")
                
        elif 'that will be all' in query or 'go to sleep' in query or 'shutdown' in query or 'bye' in query:
            speak("Always a pleasure serving you. Good bye!!!!")
            sys.exit()
            
        else:
            speak(f"I am sorry i don't understand, {query}")
        
        speak("Anything else sir?")