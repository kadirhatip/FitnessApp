import os
os.system('cls')

import speech_recognition as sr 
import time 
import random
import playsound
from gtts import gTTS



rec = sr.Recognizer()

def recordVoice():

    with sr.Microphone() as source:

        vInput = rec.listen(source)

        try: 
            vOutput = rec.recognize_google(vInput)
        except sr.UnknownValueError:
            adonisSays('Sorry Boss, I did not get that')
        except sr.RequestError:
            adonisSays('Sorry Boss, my speech service seems to be down right now')
        return vOutput

def respond(vInput):
    if 'start training' in vInput:
        adonisSays('Ok Boss, starting Fitness App')
        fitnessApp()
    if 'exit' in vInput:
        adonisSays('Ok Boss, see you later')
        exit()

def adonisSays(audioString):
    tts = gTTS(text=audioString, lang='en')
    r = random.randint(1,10000000)
    audioFile = 'audio-' + str(r) + '.mp3'
    tts.save(audioFile)
    print(audioString)
    playsound.playsound(audioFile)
    os.remove(audioFile)

def fitnessApp():
    pass


time.sleep(1)
adonisSays('Welcome Boss. ')
while 1:
    recordedVoice = recordVoice()
    respond(recordedVoice)


