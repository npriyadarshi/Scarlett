import sys
import yaml
import speech_recognition as sr

from GreyMatter.SenseCells.tts import tts

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
        print("Scarlett thinks you said ' "+speech_text+" '")
    except sr.UnknownValueError:
        print("Scarlett could not understand audio !!")

    tts(speech_text)

main()
