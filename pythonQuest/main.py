import sys

import pyaudio
import speech_recognition as sr
import pyttsx3
import sys
recognizer = sr.Recognizer()
speaker = pyttsx3.init()

bad_answer = 0
emergency_number = 0
speaker.say("Welcome to the Covid 19 self-assessment. You will be asked a series of questions. Please answer yes or no.")
speaker.runAndWait()

def yes_no_question(question):
    global emergency_number
    if emergency_number == 0:
        with sr.Microphone() as source:
            speaker.say(question)
            speaker.runAndWait()
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                if text == "yes":
                    global bad_answer
                    bad_answer = bad_answer + 1
                    print(bad_answer)
            except:
                print("please answer yes or no")

def emergency_question(question):
    global emergency_number
    if emergency_number == 0:
        with sr.Microphone() as source:
            speaker.say(question)
            speaker.runAndWait()
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                if text == "yes":
                    speaker.say("You may be in a crisis. Please call 911 immediately.")
                    speaker.runAndWait()
                    emergency_number += 1
            except:
                print("please answer yes or no")

yes_no_question("Are you experiencing shortness of breath?")
emergency_question("Are you experiencing severe chest pain?")
yes_no_question("Have any family members been infected with Covid 19 in the last 14 days?")

if bad_answer > 0 and emergency_number == 0:
    speaker.say("You are at high risk of covid 19. Please stay home for 14 days and call 911 if an emergency arises.")
    speaker.runAndWait()
elif bad_answer == 0 and emergency_number == 0:
    speaker.say("you are declared safe to go outside!")
    speaker.runAndWait()