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

    speak("I am Jarvis Lalith. Please tell me how may I help you.")


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

    # Logic for executing tasks based on query
    if "hello jarvis" in query:
        speak("Hello Lalith. What can I do for you today?")

    if "good morning" in query:
        speak("Good Morning Lalith!")
        strTime = time.strftime("%I:%M %p")
        speak(f"The time is {strTime}")
        date = datetime.date.today()
        day = datetime.datetime.today().strftime("%A")
        speak(f"Today is {day}. {date}")

    if "good afternoon" in query:
        speak("Good Afternoon Lalith! What can I do for you?")

    if "good evening" in query:
        speak("Good Evening Lalith! What can I do for you?")

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
        speak(f"Lalith, The time is {strTime}")

    if "the date" in query:
        date = datetime.date.today()
        speak(f"Lalith, The date is {date}")

    if "day" in query:
        day = datetime.datetime.today().strftime("%A")
        speak(f"Lalith, Today is {day}")

    if "open code" in query:
        codePath = "C:\\Users\\splba\\.vscode\\Code.exe"
        os.startfile(codePath)

    if "how are you" in query:
        speak("I am doing good Lalith, Thank you for asking")

    if "add" in query:
        try:
            speak("What are your numbers?")
            first_number = int(takeCommand())
            second_number = int(takeCommand())
            results = first_number + second_number
            speak(f"Lalith, Your first number was {first_number}")
            speak(f"And your second number was {second_number}")
            speak(f"Your Sum is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to add the numbers you gave me right now.")

    if "subtract" in query:
        try:
            speak("What are your numbers?")
            first_number = int(takeCommand())
            second_number = int(takeCommand())
            results = first_number - second_number
            speak(f"Lalith, Your first number was {first_number}")
            speak(f"And your second number was {second_number}")
            speak(f"Your Difference is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to subtract the numbers you gave me right now.")

    if "multiply" in query:
        try:
            speak("What are your numbers?")
            first_number = int(takeCommand())
            second_number = int(takeCommand())
            results = first_number * second_number
            speak(f"Lalith, Your first number was {first_number}")
            speak(f"And your second number was {second_number}")
            speak(f"Your Product is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to multiply the numbers you gave me right now.")

    if "divide" in query:
        try:
            speak("What are your numbers?")
            first_number = int(takeCommand())
            second_number = int(takeCommand())
            results = int(first_number / second_number)
            speak(f"Lalith, Your first number was {first_number}")
            speak(f"And your second number was {second_number}")
            speak(f"Your Quotient is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to divide the numbers you gave me right now.")

    if "exponent" in query:
        try:
            speak("What are your numbers?")
            base_number = int(takeCommand())
            exponent_number = int(takeCommand())
            results = int(base_number ** exponent_number)
            speak(f"Lalith, Your base number is {base_number}")
            speak(f"And your exponent number is {exponent_number}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to square the numbers you gave me right now.")

    if "square root" in query:
        try:
            speak("What is your square root number?")
            sqrt_number = int(takeCommand())
            results = int(math.sqrt(sqrt_number))
            speak(f"Lalith, Your square root number was {sqrt_number}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to square root the numbers you gave me right now.")

    if "percent" in query:
        try:
            percent_number = int(takeCommand())
            first_number = int(takeCommand())

            results = int((percent_number / 100) * first_number)

            speak(f"Lalith, Your percent number was {percent_number}")
            speak(f"And your number was {first_number}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to find the percent of any given number.")

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

            speak(f"Lalith, Your first number was {a}, and your second number was {b}")
            speak(f"The LCM of these two numbers is {maxNum}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to find the lcm of the numbers you gave me right now.")

    if "pythag theorem" in query:
        try:
            speak("What are your values?")
            first_leg = int(takeCommand())
            second_leg = int(takeCommand())
            added_numbers = int(math.pow(first_leg, 2) + math.pow(second_leg, 2))
            results = int(math.sqrt(added_numbers))
            speak(f"Lalith, Your first leg value was {first_leg}")
            speak(f"Your second leg value was {second_leg}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to do the pythagorean theorem with the the leg values you gave right now.")

    if "pythagorean theorem hypotenuse leg" in query:
        try:
            speak("What are your values?")
            hypotenuse_leg = int(takeCommand())
            leg_leg = int(takeCommand())
            results = int(math.sqrt(math.pow(hypotenuse_leg, 2) - math.pow(leg_leg, 2)))
            speak(f"Lalith, Your hypotenuse value was {hypotenuse_leg}")
            speak(f"And your leg value was {leg_leg}")
            speak(f"Your Answer is {results}")

        except Exception as e:
            speak("Sorry Lalith. I am not able to find the other leg value with your given hypotenuse and leg value")

    if "sin" in query:
        try:
            speak("Would you like the sine of an angle in degrees or the sine of angle in radians?")
            user = takeCommand()
            if user == "degrees":
                try:
                    speak("What angle in degrees would you like the sine of?")
                    angle = int(takeCommand())
                    result = round(math.sin(math.radians(angle)), 3)
                    speak(f"Lalith the sine of {angle} degrees is approximately {result}")
                
                except Exception as e:
                    speak("Sorry Lalith. I am not able to find the sine of the angle you gave me in degrees")
            elif user == "radians":
                try:
                    speak("What angle in radians would you like the sine of?")
                    angle = int(takeCommand())
                    result = round(math.sin(angle), 3)
                    speak(f"Lalith the sine of {angle} radians is approximately {result}")
        
                except Exception as e:
                    speak("Sorry Lalith. I am not able to find the sine of the angle you gave me in radians")

        except Exception as e:
            speak("Sorry Lalith. I am not able to find the sine of the angle in degrees or in radians you gave right now")

    if "cos" in query:
        try:
            speak("Would you like to find the cosine of an angle in degrees or the cosine of an angle in radians?")
            user = takeCommand()
            if user == "degrees":
                try:
                    speak("What angle in degrees would you like the cosine of?")
                    angle = int(takeCommand())
                    result = round(math.cos(math.radians(angle)), 3)
                    speak(f"Lalith the cosine of {angle} degrees is approximately {result}")
                
                except Exception as e:
                    speak("Sorry Lalith. I am not able to find the cosine of the angle you gave right now")
            elif user == "radians":
                try:
                    speak("What angle in radians would you like the cosine of?")
                    angle = int(takeCommand())
                    result = round(math.cos(angle), 3)
                    speak(f"Lalith the cosine of {angle} radians is approximately {result}")
                except Exception as e:
                    speak("Sorry Lalith. I am not find the cosine of the angle you gave in radians")
        
        except Exception as e:
            speak("Sorry Lalith. I am not able to find the cosine of the angle in degrees or in radians you gave right now")

    if "tan" in query:
        try:
            speak("Would you like to find the tangent of an angle in degrees or the tangent of an angle in radians?")
            user = takeCommand()
            if user == "degrees":
                try:
                    speak("What angle in degrees would you like the tangent of?")
                    angle = int(takeCommand())
                    result = round(math.tan(math.radians(angle)), 3)
                    speak(f"Lalith the tangent of {angle} degrees is approximately {result}")
                
                except Exception as e:
                    speak("Sorry Lalith. I am not able to find the tangent of the angle you gave in degrees")
            elif user == "radians":
                try:
                    speak("What angle in radians would you like the tangent of?")
                    angle = int(takeCommand())
                    result = round(math.tan(angle), 3)
                    speak(f"Lalith the tangent of {angle} radians is approximately {result}")
                
                except Exception as e:
                    speak("Sorry Lalith. I am not able to find the tangent of the angle you gave in radians")

        except Exception as e:
            speak("Sorry Lalith. I am not able to find the tangent of the angle in degrees or in radians you gave right now")

    if "rps game" in query:
        speak("Welcome to Rock Paper Scissors!")
        moves = ["rock", "paper", "scissors"]

        try:
            playing = True
            points = 0
            while playing:
                speak("What moves do you want to choose?")
                user = takeCommand().lower()
                jarvis = random.choice(moves)

                speak(f"Lalith, Your move was {user}")
                speak(f"And my move was {jarvis}")

                if user == jarvis:
                    speak("Lalith, It's a tie!")

                if user == "rock" and jarvis == "scissors":
                    speak("Lalith, You Won!")
                    points += 1
                elif user == "paper" and jarvis == "rock":
                    speak("Lalith, You Won!")
                    points += 1
                elif user == "scissors" and jarvis == "paper":
                    speak("Lalith, You Won!")
                    points += 1
                if user == "scissors" and jarvis == "rock":
                    speak("Lalith, You Lost!")
                    points -= 1
                elif user == "rock" and jarvis == "paper":
                    speak("Lalith, You Lost!")
                    points -= 1
                elif user == "paper" and jarvis == "scissors":
                    speak("Lalith, You Lost!")
                    points -= 1

                if points == 3:
                    speak("Lalith, You have 3 points which means You won the game!")
                    playing = False
                    speak("You have exited the game successfully")
                    speak("Come back again if you feel like playing with me")
                else:
                    try:
                        speak("Would you like to play again?")
                        user = takeCommand().lower()

                        if user == "yes":
                            playing = True
                            points = points
                        elif user == "exit" or "no":
                            playing = False
                            speak("Lalith, You have exited the game successfully.")
                            speak(f"Lalith, You got {points} points while playing.")
                            points = 0
                    
                    except Exception as e:
                        speak("Sorry Lalith. I am not able to make the game play again.")
            
        except Exception as e:
            speak("Sorry Lalith. I am not able to play rock paper scissors with you right now.")

    if "adventure" in query:
        speak("Welcome to Adventure!")
        speak("The objective of this game is to find your way around to get to your home")

        try:
            speak("Would you like to play?")
            user = takeCommand()
            health = 15

            if user == "yes":
                speak("You will be starting off with 15 health")
                speak("Let's Play!")

                speak("You notice there are two pathways... Do you want to go left or go right?")
                user = takeCommand()

                if user == "left":
                    speak("You took the left path.")
                    speak("You notice a road... Do you want to use the sidewalk to cross or go across the road?")
                    
                    user = takeCommand()
                    
                    if user == "sidewalk":
                        speak("Your decide to cross the road using the sidewalk and crossed the road safely")
                    elif user == "across":
                        speak("You decide to go across the road to cross the road, but you got hit by a car and lost 5 health.")
                        health -= 10
                    
                    speak("You see a strange animal... Do you want to pet it or just leave it alone?")

                    user = takeCommand()

                    if user == "alone":
                        speak("You decide to leave it alone, so it will not mess with you.")
                    elif user == "pet":
                        speak("You decide to pet it, but it got mad at you and decided to bit you, so you lost 5 health")
                        health -= 5

                    speak("You see a river... Do you want to go across or go around?")

                    user = takeCommand()

                    if user == "around":
                        speak("You decide to go around the river, so you reach your house, which means you win!")
                    elif user == "across":
                        speak("You managed to get across, but you were bitten by a fish and lost 5 health, which means you lost!")

                elif user == "right":
                    speak("You took the right path. You fell down a hole and lost all your health, which means you lost!")

            elif user == "no":
                speak("Goodbye! Hope you will play this game with me on another time!")
        
        except Exception as e:
            speak("Sorry Lalith. I am not able to play adventure with your right now.")

    if "what can you do" in query:
        speak("I can play music")
        speak("I can add, subtract, multiply, divide, square and square root numbers")
        speak("I can find the lcm of any two numbers given")
        speak("I can do the pythagorean theorem")
        speak("I can do the pythagorean theorem with a given hypotenuse and leg value")
        speak("I can find the sine, cosine, and tangent of an angle either given in degrees or in radians")
        speak("I can play rock paper scissors with you")
        speak("I can play adventure with you")
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
            speak("Sorry Lalith. I am not able to send the email right now.")

    if "exit" in query:
        speak("Goodbye Lalith! Have a Good Rest of Your Day!")
        break