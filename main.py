# 1. Import the TTS library
import pyttsx3

# 2. Initialize the TTS engine
engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker Project 1.1, created by Vishwajit vm")

    while True:
        inputdata = input("Enter what you want me to speak: ")

        # Exit condition
        if inputdata.lower() == 'bye':
            engine.say("Bye Bye Friend")  #Use TTS to say goodbye
            engine.runAndWait()
            break

        # Speak the input text
        engine.say(inputdata)
        engine.runAndWait()
