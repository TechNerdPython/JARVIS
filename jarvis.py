import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time
import math
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you.")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("lalithbandaru36@gmail.com", "Lbandaru389281!")
    server.sendmail("lalithbandaru36@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "hello jarvis" in query:
            speak("Hello Sir. What can I do for you today?")

        if "good morning" in query:
            speak("Good Morning Sir! What can I do for you?")

        if "good afternoon" in query:
            speak("Good Afternoon Sir! What can I do for you?")

        if "good evening" in query:
            speak("Good Evening Sir! What can I do for you?")

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        if "open youtube" in query:
            webbrowser.open("youtube.com")

        if "open google" in query:
            webbrowser.open("google.com")

        if "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        if "play music" in query:
            music_dir = "C:\\Users\\splba\\Music\\Sample"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        if "play thunderstorm with rain sound" in query:
            audio_dir = "C:\\Users\\splba\\Jarvis\\audio_dir\\Audio.mp3"
            audio_file = os.path.join(audio_dir)
            os.startfile(os.path.join(audio_dir, audio_file))

        if "the time" in query:
            strTime = time.strftime("%I:%M %p")
            speak(f"Sir, The time is {strTime}")

        if "the date" in query:
            date = datetime.date.today()
            speak(f"Sir, The date is {date}")

        if "day" in query:
            day = datetime.datetime.today().strftime("%A")
            speak(f"Sir, Today is {day}")

        if "open code" in query:
            codePath = "C:\\Users\\splba\\.vscode\\Code.exe"
            os.startfile(codePath)

        if "how are you" in query:
            speak("I am doing good Sir, Thank you for asking")

        if "add" in query:
            try:
                speak("What are your numbers?")
                first_number = int(takeCommand())
                second_number = int(takeCommand())
                results = first_number + second_number
                speak(f"Sir, Your first number was {first_number}")
                speak(f"And your second number was {second_number}")
                speak(f"Your Sum is {results}")

            except Exception as e:
                speak("Sorry Sir. I am not able to add the numbers you gave me right now.")

        if "subtract" in query:
            try:
                speak("What are your numbers?")
                first_number = int(takeCommand())
                second_number = int(takeCommand())
                results = first_number - second_number
                speak(f"Sir, Your first number was {first_number}")
                speak(f"And your second number was {second_number}")
                speak(f"Your Difference is {results}")

            except Exception as e:
                speak("Sorry Sir. I am not able to subtract the numbers you gave me right now.")

        if "multiply" in query:
            try:
                speak("What are your numbers?")
                first_number = int(takeCommand())
                second_number = int(takeCommand())
                results = first_number * second_number
                speak(f"Sir, Your first number was {first_number}")
                speak(f"And your second number was {second_number}")
                speak(f"Your Product is {results}")

            except Exception as e:
                speak("Sorry Sir. I am not able to multiply the numbers you gave me right now.")

        if "divide" in query:
            try:
                speak("What are your numbers?")
                first_number = int(takeCommand())
                second_number = int(takeCommand())
                results = int(first_number / second_number)
                speak(f"Sir, Your first number was {first_number}")
                speak(f"And your second number was {second_number}")
                speak(f"Your Quotient is {results}")

            except Exception as e:
                speak("Sorry sir. I am not able to divide the numbers you gave me right now.")

        if "exponent" in query:
            try:
                speak("What are your numbers?")
                base_number = int(takeCommand())
                exponent_number = int(takeCommand())
                results = int(base_number ** exponent_number)
                speak(f"Sir, Your base number is {base_number}")
                speak(f"And your exponent number is {exponent_number}")
                speak(f"Your Answer is {results}")

            except Exception as e:
                speak("Sorry sir. I am not able to square the numbers you gave me right now.")

        if "square root" in query:
            try:
                speak("What is your square root number?")
                sqrt_number = int(takeCommand())
                results = int(math.sqrt(sqrt_number))
                speak(f"Sir, Your square root number was {sqrt_number}")
                speak(f"Your Answer is {results}")

            except Exception as e:
                speak("Sorry Sir. I am not able to square root the numbers you gave me right now.")
                
        if "lcm" in query:
            try:
                speak("What is your first number?")
                a = int(takeCommand())
                speak("What is your second number?")
                b = int(takeCommand())

                maxNum = max(a, b)

                while (True):
                    if (maxNum % a == 0 and maxNum % b == 0):
                        break
                    maxNum = maxNum + 1

                speak(f"Sir, Your first number was {a}, and your second number was {b}")
                speak(f"The LCM of these two numbers is {maxNum}")

            except Exception as e:
                speak("Sorry Sir. I am not able to find the lcm of the numbers you gave me right now.")

        if "pythag theorem" in query:
            try:
                speak("What are your values?")
                first_leg = int(takeCommand())
                second_leg = int(takeCommand())
                added_numbers = int(math.pow(first_leg, 2) + math.pow(second_leg, 2))
                results = int(math.sqrt(added_numbers))
                speak(f"Sir, Your first leg value was {first_leg}")
                speak(f"Your second leg value was {second_leg}")
                speak(f"Your Answer is {results}")

            except Exception as e:
                speak("Sorry Sir. I am not able to do the pythagorean theorem with the the leg values you gave right now.")

        if "pythagorean theorem hypotenuse leg" in query:
            try:
                speak("What are your values?")
                hypotenuse_leg = int(takeCommand())
                leg_leg = int(takeCommand())
                results = int(
                    math.sqrt(math.pow(hypotenuse_leg, 2) - math.pow(leg_leg, 2)))
                speak(f"Sir, Your hypotenuse value was {hypotenuse_leg}")
                speak(f"And your leg value was {leg_leg}")
                speak(f"Your Answer is {results}")

            except Exception as e:
                speak("Sorry Sir. I am not able to find the other leg value with your given hypotenuse and leg value")
        
        if "what can you do" in query:
            speak("I can play music")
            speak("I can add, subtract, multiply, divide, square and square root numbers")
            speak("I can do the pythagorean theorem")
            speak("I can do the pythagorean theorem with a given hypotenuse and leg value")
            speak("I can send an email")
            speak("I can tell the time")
            speak("I can tell the date")
            speak("I can search in wikipedia")
            speak("I can open google")
            speak("I can open stackoverflow")
            speak("I can open youtube")

        if "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "lalithbandaru36@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                speak("Sorry Sir. I am not able to send the email right now.")

        if "exit" in query:
            speak("Goodbye Sir! Have a Good Rest of Your Day!")
            break
