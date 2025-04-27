import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import webbrowser
import sys
import google.generativeai as genai
import time


genai.configure(api_key="AIzaSyDSmXq0UrJiqUD6uUCz9AOupOL0lh0MDmU")

def ask_gemini(question):
    model = genai.GenerativeModel('gemini-1.5-flash') 
    response = model.generate_content(question)
    return response.text\
    
engine = pyttsx3.init()

def speak(text):
    print(f"Dhanno: {text}")
    engine.say(text)
    engine.runAndWait()
   

def wish_me():
    speak("I am Dhanno. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            speak("Please say again...")
            return "None"
        return query.lower()

if __name__ == "__main__":
    wish_me()
    activated = False

    while True:
        if not activated:
            print("Waiting for activation word 'Jarvis'...")
            activation = take_command()
            if 'jarvis' in activation:
                speak("Yes, I am listening...")
                activated = True
        else:
            query = take_command()
            s = query
            if query == "none":
                continue

            if 'joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'youtube' in query:
                webbrowser.open("https://www.youtube.com")

            elif 'brave' in query:
                webbrowser.open("https://search.brave.com")

            elif 'mushayara' in query:
                webbrowser.open("https://youtu.be/ijGr3sSEXXw?si=dEjYd-L8QGZtXxzU")

            elif 'music' in query:
                webbrowser.open("https://music.youtube.com/watch?v=jfgmf8ERMN4&list=RDCLAK5uy_n17q7_2dwfDqWckpccDyTTkZ-g03jXuII")

            elif 'song' in query:
                webbrowser.open("https://music.youtube.com/watch?v=XFOVXD1qttc&list=PLmsYUBeqmEV0dKDqaL95j-m41Y6ZurPbD")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif 'ruk ja bhai' in query or 'bye' in query:
                speak("Okay, bye!")
                sys.exit()

            elif s in query: 
                answer = ask_gemini(query)
                short_answer = ' '.join(answer.split()[:30])
                speak(short_answer)
