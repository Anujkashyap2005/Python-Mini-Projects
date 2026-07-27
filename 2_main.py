# import random

# computer_choice = random.randint(10,50)
# a = -1
# guess = 0
# while a != computer_choice:
#     guess += 1
#     you = int(input("Guess the Number:  "))

#     if computer_choice == you:
#       print("You Win")

#     elif computer_choice < you:
#           print("Plz Enter a lower number: ")

#     elif computer_choice > you:
#        print("plz Enter a higher number: ")

# print(f"The compute number was: {computer_choice}")
# print(f"You guest than in: {you}")


import speech_recognition as sr
import webbrowser 
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speek(text):
    engine.say(text)
    engine.runAndWait()



if __name__ == "__main__":
    speek("Initializing Anuj..........")

    while True:
        r = sr.Recognizer()
        with sr.Microphone () as source:
            print("Listening..........")
            audio = r.listen(source, timeout=2)

        print("recognizing............")

        try:
            command = r.recognize_google(audio)
            print(command)
        except Exception as e:
            print("Error; {0}".format(e))




