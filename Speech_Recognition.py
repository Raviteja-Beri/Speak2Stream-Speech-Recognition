import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init('dummy')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    cmd = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listening.listen(source)
            cmd = listening.recognize_google(audio)
            cmd = cmd.lower()
    except Exception as e:
        print("Sorry, I couldn't understand. Error:", e)
    
    return cmd

def run():
    cmd = hear()
    print("Command:", cmd)
    if cmd == "":
        speak("I didn't catch that. Please try again.")
    elif 'play' in cmd:
        song = cmd.replace('play', '').strip()
        speak('Playing ' + song)
        pk.playonyt(song)
    else:
        speak("I can only play music right now.")

run()
