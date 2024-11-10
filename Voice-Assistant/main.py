import speech_recognition as sr
from selenium import webdriver
import pyttsx3
from time import ctime

# CUSTOM MODULES
import whatsapp
import weather
import play
import read
import sendmail

def respond(AudioString):
    print(f"Assistant: {AudioString}")  # Debug output
    pyttsx3.speak(AudioString)

def listen(r):
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("I am listening...")
        audio = r.listen(source, timeout=5)  # Listen with a timeout
        print("Listening completed.")  # Debug output
    
    cmd = ""
    try:
        cmd = r.recognize_google(audio)
        print(f"Command recognized: {cmd}")  # Debug output
        return cmd.lower()
    except sr.UnknownValueError:
        respond("Sorry, I did not understand that.")
    except sr.RequestError as e:
        respond(f"Could not request results from Google Speech Recognition service; {e}")
    return cmd

def digital_assistant(data, r):  # Add the recognizer instance as a parameter
    if "how are you" in data:
        respond("I am well")

    if "what time is it" in data:
        respond(ctime())

    if "stop listening" in data or "stop" in data or "quit" in data:
        respond("Goodbye!")
        return False

    if "whatsapp" in data:
        whatsapp.askinfo(r)  # Pass the recognizer instance here

    if "what can you do" in data:
        respond("I can handle pretty much all your tasks, sir!")

    if "where is" in data:
        loc = " ".join(data.split(" ")[2:])
        location_url = f"https://www.google.com/maps/place/{loc}"
        respond(f"Hold on, I will show you where {loc} is.")
        browser = webdriver.Chrome()
        browser.get(location_url)

    if "weather" in data:
        weather.info(data)

    if "want to watch" in data or "stream" in data:
        l = data.split(" ")
        video = "+".join(l[2: l.index("on")]) if "on" in l else " ".join(l[2:])
        platform = l[l.index("on") + 1:] if "on" in l else ""
        play.movies(video, platform)

    if "play" in data:
        song = " ".join(data.split(" ")[1:])
        play.music(song)

    if "read" in data or "search" in data:
        topic = data.split(" ")[-1]
        read.wikipedia(topic)

    if "email" in data:
        respond("Please enter the email address of the recipient.")
        to = input()
        respond("Please tell me the subject regarding the email.")
        sub = listen(r)  # Pass the recognizer instance to listen
        respond("Kindly tell me the body of the email.")
        body = listen(r)  # Pass the recognizer instance to listen
        sendmail.send(to, sub, body)

    return True


def main():
    pyttsx3.speak("Hello Pranathi. What can I do for you?")
    r = sr.Recognizer()
    
    while True:
        task = listen(r)
        if task:  # Only process if a task was recognized
            listening = digital_assistant(task, r)  # Pass recognizer instance here
            if not listening:
                break

if __name__ == "__main__":
    main()

