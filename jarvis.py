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
import json
import requests
import pytz
from googletrans import Translator

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

name_dict = {"name": ""}

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

    speak("I am Jarvis!")
    speak("May I please know your name? Say yes or no")
    permission = takeCommand()
    if permission == "yes":
        speak("Would you like to type or speak your name?")
        type_or_speak = takeCommand()
        if type_or_speak == "type":
            speak("Please type your name")
            typed_name = input("What is your name? ")
            name_dict.update({"name": typed_name})
        elif type_or_speak == "speak":
            speak("Please speak your name")
            name = takeCommand()
            name_dict.update({"name": name})
    elif permission == "no":
        random_name = "Anonymous"
        name_dict.update({"name": random_name})
    
    name = name_dict.get("name")
    speak(f"Hello {name}! I am Jarvis. Please tell me how may I help you?")


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
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("lalithbandaru36@gmail.com", "Lbandaru389281!")
    server.sendmail("lalithbandaru36@gmail.com", to, content)
    server.close()


wishMe()
while True:
    query = takeCommand().lower()
    name = name_dict.get("name")

    # Logic for executing tasks based on query
    if "hello jarvis" in query:
        speak(f"Hello {name}. What can I do for you today?")

    if "good morning" in query:
        speak(f"Good Morning {name}!")
        strTime = time.strftime("%I:%M %p")
        speak(f"The time is {strTime}")
        date = datetime.date.today()
        day = datetime.datetime.today().strftime("%A")
        speak(f"Today is {day}. {date}")

    if "good afternoon" in query:
        speak(f"Good Afternoon {name}! What can I do for you?")

    if "good evening" in query:
        speak(f"Good Evening {name}! What can I do for you?")

    if "repeat" in query:
        speak("What would you like me to repeat after you?")
        user = takeCommand()
        speak(f"You said {user}")

    if "weather" in query:
        api_key = "70ad116bc1e838bd16f7b03afdf67559"

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name 
        speak("Which city's weather would you like?")
        city_name = takeCommand()
        
        # complete_url variable to store 
        # complete url address 
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
        
        # get method of requests module 
        # return response object 
        response = requests.get(complete_url)
        
        # json method of response object  
        # convert json format data into 
        # python format data 
        x = response.json() 
        
        # Now x contains list of nested dictionaries 
        # Check the value of "cod" key is equal to 
        # "404", means city is found otherwise, 
        # city is not found 
        if x["cod"] != "404": 
        
            # store the value of "main" 
            # key in variable y 
            y = x["main"] 
        
            # store the value corresponding 
            # to the "temp" key of y
            current_temperature = y["temp"]
        
            # store the value corresponding 
            # to the "pressure" key of y 
            current_pressure = y["pressure"] 
        
            # store the value corresponding 
            # to the "humidity" key of y 
            current_humidiy = y["humidity"] 
        
            # store the value of "weather" 
            # key in variable z 
            z = x["weather"] 
        
            # store the value corresponding  
            # to the "description" key at  
            # the 0th index of z 
            weather_description = z[0]["description"] 
        
            # print following values 
            speak(f" The Temperature of {city_name} in kelvins is" +
                            str(current_temperature) +
                f"\n The humidity of {city_name} in percentage is " +
                            str(current_humidiy) +
                f"\n The condition outside of {city_name} is currently" +
                            str(weather_description))
        
        else: 
            speak("City Not Found")

    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    if "translate" in query:
        speak("What would you like to translate?")
        sentence = takeCommand()
        translator = Translator()
        speak("Which language would you like to translate it into?")
        user = takeCommand()
        result = translator.translate(sentence, dest=user)
        translated = result.text
        speak(f"The translation for what you said is {translated}")

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
        start_file = os.startfile(os.path.join(audio_dir, audio_file))

    if "the time" in query:
        strTime = time.strftime("%I:%M %p")
        speak(f"The time is {strTime}")

    if "time in" in query:
        try:
            speak("Which timezone's time would you like to know?")
            user = takeCommand()
            API_KEY = "7YKJQ872N6S9"

            base_url = "http://api.timezonedb.com/v2.1/get-time-zone?"
            complete_url = base_url + "key=" + API_KEY + "&format=json" + "&by=zone" + "&zone=" + user
            response = requests.get(complete_url)
            response_json = response.json()
            formatted_time = response_json["formatted"]
            speak(f"The time in {user} timezone is {formatted_time}")

        except Exception as e:
            speak("Error! I am not able to find the time in the given timezone")
            print(e)

    if "the date" in query:
        date = datetime.date.today()
        speak(f"The date is {date}")

    if "day" in query:
        day = datetime.datetime.today().strftime("%A")
        speak(f"Today is {day}")

    if "open code" in query:
        codePath = "C:\\Users\\splba\\.vscode\\Code.exe"
        os.startfile(codePath)

    if "how are you" in query:
        speak(f"I am doing good {name}, Thank you for asking")

    if "add" in query:
        try:
            speak("What is your first number?")
            first_number = int(takeCommand())
            speak("What is your second number?")
            second_number = int(takeCommand())
            results = first_number + second_number
            speak(f"Your first number was {first_number}")
            speak(f"And your second number was {second_number}")
            speak(f"Your Sum is {results}")

        except Exception as e:
            speak(f"Error! I am not able to add the numbers you gave me right now.")

    if "subtract" in query:
        try:
            speak("What is your first number?")
            first_number = int(takeCommand())
            speak("What is your second number?")
            second_number = int(takeCommand())
            results = first_number - second_number
            speak(f"Your first number was {first_number}")
            speak(f"And your second number was {second_number}")
            speak(f"Your Difference is {results}")

        except Exception as e:
            speak(f"Error! I am not able to subtract the numbers you gave me right now.")

    if "multiply" in query:
        try:
            speak("What is your first number?")
            first_number = int(takeCommand())
            speak("What is your second number?")
            second_number = int(takeCommand())
            results = first_number * second_number
            speak(f"Your first number was {first_number}")
            speak(f"And your second number was {second_number}")
            speak(f"Your Product is {results}")

        except Exception as e:
            speak(f"Error! I am not able to multiply the numbers you gave me right now.")

    if "divide" in query:
        try:
            speak("What is your dividend?")
            first_number = int(takeCommand())
            speak("What is your divisor")
            second_number = int(takeCommand())
            results = int(first_number / second_number)
            speak(f"Your first number was {first_number}")
            speak(f"And your second number was {second_number}")
            speak(f"Your Quotient is {results}")

        except Exception as e:
            speak(f"Error! I am not able to divide the numbers you gave me right now.")

    if "exponent" in query:
        try:
            speak("What is your base?")
            base_number = int(takeCommand())
            speak("What is your exponent?")
            exponent_number = int(takeCommand())
            results = int(base_number ** exponent_number)
            speak(f"{name}, Your base number is {base_number}")
            speak(f"And your exponent number is {exponent_number}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak(f"Error! I am not able to square the numbers you gave me right now.")

    if "square root" in query:
        try:
            speak("What is your square root number?")
            sqrt_number = int(takeCommand())
            results = int(math.sqrt(sqrt_number))
            speak(f"Your square root number was {sqrt_number}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Error! I am not able to square root the numbers you gave me right now.")

    if "percent" in query:
        try:
            speak("What is your number you want to find the percentage of?")
            percent_number = int(takeCommand())
            speak("What is your percentage number?")
            first_number = int(takeCommand())

            results = int((percent_number / 100) * first_number)

            speak(f"Your percent number was {percent_number}")
            speak(f"And your number was {first_number}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Error! I am not able to find the percent of any given number.")

    if "lcm" in query:
        try:
            speak("What is your first number?")
            a = int(takeCommand())
            speak("What is your second number?")
            b = int(takeCommand())

            maxNum = max(a, b)

            while True:
                if (maxNum % a == 0 and maxNum % b == 0):
                    break
                maxNum = maxNum + 1

            speak(f"Your first number was {a}, and your second number was {b}")
            speak(f"The LCM of these two numbers is {maxNum}")

        except Exception as e:
            speak("Error! I am not able to find the lcm of the numbers you gave me right now.")

    if "pythag theorem" in query:
        try:
            speak("What is your first leg value?")
            first_leg = int(takeCommand())
            speak("What is your second leg value?")
            second_leg = int(takeCommand())
            added_numbers = int(math.pow(first_leg, 2) + math.pow(second_leg, 2))
            results = int(math.sqrt(added_numbers))
            speak(f"Your first leg value was {first_leg}")
            speak(f"Your second leg value was {second_leg}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Error! I am not able to do the pythagorean theorem with the the leg values you gave right now.")

    if "pythagorean theorem hypotenuse leg" in query:
        try:
            speak("What is your hypotenuse value?")
            hypotenuse_leg = int(takeCommand())
            speak("What is your leg value?")
            other_leg = int(takeCommand())
            results = int(math.sqrt(math.pow(hypotenuse_leg, 2) - math.pow(leg_leg, 2)))
            speak(f"Your hypotenuse value was {hypotenuse_leg}")
            speak(f"And your leg value was {other_leg}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Error! I am not able to find the other leg value with your given hypotenuse and leg value")
    
    if "factorial" in query:
        speak("What is your factorial number?")
        s = int(takeCommand())

        n = 1
        v = 1

        while (n <= s):
            v = v * n
            n = n + 1

        speak(f"The answer of {s} factorial is {v}")

    if "sin" in query:
        try:
            speak("What is the the measurement of the angle you would like the sine of which is in degrees or the sine of the angle which is in radians?")
            user = takeCommand()
            if user == "degrees":
                try:
                    speak("What is the measurement of the angle in degrees you would like the sine of?")
                    angle = int(takeCommand())
                    result = round(math.sin(math.radians(angle)), 3)
                    speak(f"The sine of {angle} degrees is approximately {result}")
                
                except Exception as e:
                    speak("Error! I am not able to find the sine of the angle you gave me in degrees")
            elif user == "radians":
                try:
                    speak("What is the measurement of the angle in radians you would like the sine of?")
                    angle = int(takeCommand())
                    result = round(math.sin(angle), 3)
                    speak(f"The sine of {angle} radians is approximately {result}")
        
                except Exception as e:
                    speak("Error! I am not able to find the sine of the angle you gave me in radians")

        except Exception as e:
            speak("Error! I am not able to find the sine of the angle in degrees or in radians you gave right now")

    if "cos" in query:
        try:
            speak("What is the measurement of the angle you would like the cosine of which is in degrees or the cosine of the angle which is in radians?")
            user = takeCommand()
            if user == "degrees":
                try:
                    speak("What is the measurement of the angle in degrees you would like the cosine of?")
                    angle = int(takeCommand())
                    result = round(math.cos(math.radians(angle)), 3)
                    speak(f"The cosine of {angle} degrees is approximately {result}")
                
                except Exception as e:
                    speak("Error! I am not able to find the cosine of the angle you gave right now")
            elif user == "radians":
                try:
                    speak("What is the measurement of the angle in radians you would like the cosine of?")
                    angle = int(takeCommand())
                    result = round(math.cos(angle), 3)
                    speak(f"The cosine of {angle} radians is approximately {result}")
                except Exception as e:
                    speak("Error! I am not find the cosine of the angle you gave in radians")
        
        except Exception as e:
            speak("Error! I am not able to find the cosine of the angle in degrees or in radians you gave right now")

    if "tan" in query:
        try:
            speak("What is the measurement of the angle you would like to find the tangent of which is in degrees or the tangent of the angle which is in radians?")
            user = takeCommand()
            if user == "degrees":
                try:
                    speak("What is the measurement of the angle in degrees you would like the tangent of?")
                    angle = int(takeCommand())
                    result = round(math.tan(math.radians(angle)), 3)
                    speak(f"The tangent of {angle} degrees is approximately {result}")
                
                except Exception as e:
                    speak("Error! I am not able to find the tangent of the angle you gave in degrees")
            elif user == "radians":
                try:
                    speak("What is the measurement of the angle in radians you would like the tangent of?")
                    angle = int(takeCommand())
                    result = round(math.tan(angle), 3)
                    speak(f"The tangent of {angle} radians is approximately {result}")
                
                except Exception as e:
                    speak("Error! I am not able to find the tangent of the angle you gave in radians")

        except Exception as e:
            speak("Error! I am not able to find the tangent of the angle in degrees or in radians you gave right now")

    if "rps game" in query:
        speak("Hello!")
        speak("Welcome to Rock Paper Scissors!")
        moves = ["rock", "paper", "scissors"]

        try:
            playing = True
            points = 0
            while playing:
                speak("What move do you want to choose, Rock Paper or Scissors?")
                user = takeCommand().lower()
                jarvis = random.choice(moves)

                speak(f"Your move was {user}")
                speak(f"And my move was {jarvis}")

                if user == jarvis:
                    speak("It's a tie!")

                if user == "rock" and jarvis == "scissors":
                    speak("You Won!")
                    points += 1
                elif user == "paper" and jarvis == "rock":
                    speak("You Won!")
                    points += 1
                elif user == "scissors" and jarvis == "paper":
                    speak("You Won!")
                    points += 1
                if user == "scissors" and jarvis == "rock":
                    speak("You Lost!")
                    points -= 1
                elif user == "rock" and jarvis == "paper":
                    speak("You Lost!")
                    points -= 1
                elif user == "paper" and jarvis == "scissors":
                    speak("You Lost!")
                    points -= 1

                if points == 3:
                    speak("You have 3 points which means You won the game!")
                    playing = False
                    speak("You have exited the game successfully")
                    speak("Come back again soon!")
                else:
                    try:
                        speak("Would you like to play again?")
                        user = takeCommand().lower()

                        if user == "yes":
                            playing = True
                            points = points
                        elif user == "exit" or "no":
                            playing = False
                            speak(f"You have exited the game successfully.")
                            speak(f"You got {points} points while playing.")
                            points = 0
                    
                    except Exception as e:
                        speak("Error! I am not able to make the game play again.")
            
        except Exception as e:
            speak("Error! I am not able to play rock paper scissors with you right now.")

    if "what can you do" in query:
        speak("I can play music")
        speak("I can add, subtract, multiply, divide, square and square root numbers")
        speak("I can find the lcm of any two numbers given")
        speak("I can do the pythagorean theorem")
        speak("I can do the pythagorean theorem with a given hypotenuse and leg value")
        speak("I can find the sine, cosine, and tangent of an angle either given in degrees or in radians")
        speak("I can play rock paper scissors with you")
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
            speak("Error! I am not able to send the email right now.")

    if "exit" in query:
        speak(f"Goodbye {name}! Have a Good Rest of Your Day!")
        break