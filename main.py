import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests # i used this to use the api to derive news from the api 
from google import genai

gapi="AIzaSyCrYWQPt7KfC-kuBiGev_4LXcdmHJN9698"
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="41e19196ec69414c86f3191e6de823da"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    with sr.Microphone() as source:
                    print("JARVIS 2.0 Active ......")
                    audio = r.listen(source,timeout=8,phrase_time_limit=3)
                    command=r.recognize_google(audio)  
    client = genai.Client(api_key="AIzaSyCrYWQPt7KfC-kuBiGev_4LXcdmHJN9698")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"You are a Virtual assistant name Jarvis and you will perform all the general tasks which I will command just like Alexa and Google don't introduce yourself just answer my command and and don't use any hash tags of hash symbols in conversion , now my command is {command}  "
        )
    return response.text

def processcommand(c):

    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")

    elif "open google" in c.lower():
        webbrowser.open("https://www.google.co.in/")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in  c.lower():
        rn=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if rn.status_code == 200:
            # Parse the JSON data from the response
            data = rn.json()
        
            # Extract the headlines from the 'articles' key
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                print(article["title"])
                speak(article['title'])
    
    else:
        # Let talk to open ai 
        while True:
            output=aiprocess(c)
            print(output)
            speak(output)


if __name__== "__main__":
    speak("Initializing JARVIS......")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()


        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            print("Recognizing......")
            print(r.recognize_google(audio)) # This print what we had said through a microphone 
            wake=r.recognize_google(audio)
            if wake.lower() == "jarvis":
                speak("Hey Mukul,How can i help you ") # Wake up For Jarvis 
                # Listen for command 
                with sr.Microphone() as source:
                    print("JARVIS ACTIVE ......")
                    audio = r.listen(source,timeout=2,phrase_time_limit=3)
                    command=r.recognize_google(audio)  
                    processcommand(command)
        

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("error; {0}".format(e))
        except sr.WaitTimeoutError as e:
            print("Timeout")

