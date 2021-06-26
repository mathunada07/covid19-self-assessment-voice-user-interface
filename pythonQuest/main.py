import pyaudio
import speech_recognition as sr
import pyttsx3
from PIL import Image
recognizer = sr.Recognizer()
speaker = pyttsx3.init()

bad_answer = 0
emergency_answer = False

def get_started(line):
    correct = False
    img = Image.open("COVID Self Test.jpg")
    img.show()

    while not correct:
        with sr.Microphone() as source:
            speaker.say(line)
            speaker.runAndWait()
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                if text == "get started":
                    correct = True
                    speaker.say("please answer yes or no to the following questions")
                    speaker.runAndWait()
                    img.close()
            except:
                print("please try again")

def yes_no_question(question, img_name):
    global emergency_answer
    if not emergency_answer:
        img = Image.open(img_name)
        img.show()
        with sr.Microphone() as source:
            speaker.say(question)
            speaker.runAndWait()
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                if text == "yes":
                    global bad_answer
                    if question == "Are your symptoms normal for any medical conditions you may have?":
                        bad_answer -= 1
                    else:
                        bad_answer = bad_answer + 1
            except:
                print("please answer yes or no")
        img.close()

def emergency_question(question, img_name):
    global emergency_answer
    if not emergency_answer:
        img = Image.open(img_name)
        img.show()
        with sr.Microphone() as source:
            speaker.say(question)
            speaker.runAndWait()
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                if text == "yes":
                    speaker.say("You may be in a crisis. Please call 911 immediately.")
                    speaker.runAndWait()
                    emergency_answer = True
            except:
                print("please answer yes or no")
        img.close()

get_started("Welcome to the covid 19 self-assessment. You will be asked a series of questions. Please respond with "
            "get started.")
emergency_question("Are you currently experiencing any of these symptoms? Severe difficulty breathing, Severe chest "
                   "pain, Feeling confused or unsure of where you are, Losing consciousness", "COVID Self Test-1.jpg")
yes_no_question("Are you currently experiencing any of these symptoms? Fever and chills, Cough, Sore Throat, "
                "Headache, Muscle Pain", "COVID Self Test-2.jpg")
yes_no_question("Are your symptoms normal for any medical conditions you may have?", "COVID Self Test-6.jpg")
yes_no_question("In the last 14 days, have you been in close physical contact with someone who either is currently "
                "sick with a new cough, fever, difficulty breathing, or other symptoms associated with covid 19. This "
                "does not apply if you have been vaccinated in the last 48 hours. Otherwise, have you returned from "
                "outside of Canada in the last 2 weeks?", "COVID Self Test-3.jpg")
yes_no_question("In the last 14 days, have you traveled outside of Canada? If exempt from federal quarantine "
                "requirements, for example, an essential worker who crosses the Canada-US border regularly for work, "
                "select No.", "COVID Self Test-4.jpg")
print("bad answers: " + str(bad_answer))

if bad_answer > 0 and emergency_answer == 0:
    img = Image.open("COVID Self Test-5.jpg")
    img.show()
    speaker.say("Based on your answers, we recommend that you get tested because you have symptoms or are a close "
                "contact of someone who currently has covid 19.")
    speaker.runAndWait()
elif bad_answer == 0 and emergency_answer == 0:
    speaker.say("you are declared safe to go outside!")
    speaker.runAndWait()

speaker.say("Follow the advice of public health if you have already been tested or cleared. Our guidelines for "
            "children and adults continue to evolve as we learn more about covid 19, how it spreads, and how it "
            "affects people in different ways.")
speaker.runAndWait()