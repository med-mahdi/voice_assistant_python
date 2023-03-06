import speech_recognition as sr
from voiceassistant import *
from gptscript import *

# Initialize recognizer
r = sr.Recognizer()

# Listen for user input
while True:
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)  # Adjust microphone sensitivity
        audio = r.listen(source, timeout=5)  # Set timeout to 5 seconds

    # Recognize speech using Google Speech Recognition API
    try:
        text = r.recognize_google(audio)
        # Apply and use chat gpr api here
        history, response = chatgpt_clone(text, history)
        print("You said: {}".format(text))
        print("You said: {}".format(response))

        # Convert text to speech and play it through speaker
        engine.say(response)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.WaitTimeoutError:
        print("No speech detected within the timeout period")