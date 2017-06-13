import sys
import yaml
import speech_recognition as sr

from GreyMatter.SenseCells.tts import tts
from GreyMatter import general_conversation
from GreyMatter import time_teller
def brain(speech_text):
    words_spoken = speech_text.split()
    def speech_check(check):
        if set(check).issubset(set(words_spoken)):
            return True
        else:
            return False
    if speech_check(["who","are","you"]):
        general_conversation.who_are_you()
    elif speech_check(["how","i","look"]):
        general_conversation.how_am_i()
    elif speech_check(["what","time","now"]):
        time_teller.what_is_time()
    else:
        general_conversation.undefined()


profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

name = profile_data['name']
city_name = profile_data['city_name']

tts("Welcome "+name+". The system is ready to serve you")

def main():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("How can I help you?")
        audio = r.listen(source)

    try:
        speech_text = r.recognize_google(audio).lower().replace("'","")
        print("Scarlett thinks you said,' "+speech_text+" '")
        brain(speech_text)
    except sr.UnknownValueError:
        print("Scarlett could not understand audio !!")
    except sr.RequestError as e:
        print("Could not request ")

main()
