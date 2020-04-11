import os
import os.path
os.system('cls')

import speech_recognition as sr 
import time 
import random
import playsound
from gtts import gTTS
import openpyxl



rec = sr.Recognizer()

def recordVoice():

    with sr.Microphone() as source:

        vInput = rec.listen(source)

        try: 
            vOutput = rec.recognize_google(vInput)
        except sr.UnknownValueError:
            athenaSays('Sorry Boss, I did not get that')
        except sr.RequestError:
            athenaSays('Sorry Boss, my speech service seems to be down right now')
        return vOutput


#Processing Userinput.
def respond(vInput):
    if 'start training' in vInput:
        athenaSays('Ok Boss, starting Fitness App')    
    elif 'yeah' in vInput:
        athenaSays('Ok Boss, starting Fitness App')
    elif 'exit' in vInput:
        athenaSays('Ok Boss, see you later')
        exit()

#Playing audio through text-to-speech
def athenaSays(audioString):
    tts = gTTS(text=audioString, lang='en')
    r = random.randint(1,10000000)
    audioFile = 'audio-' + str(r) + '.mp3'
    tts.save(audioFile)
    print(audioString)
    playsound.playsound(audioFile)
    os.remove(audioFile)

def addingExercise():
    pass

def fitnessApp():
    pass




if os.path.isfile('trainingsDaten.xlsx'):
    athenaSays('Welcome back boss. Shall we start training again?')
else:
    wb = openpyxl.Workbook()
    wb.save('trainingsDaten.xlsx')
    athenaSays('Welcome to the fitness app. My name is athena, and I will be guiding you through your training.')
    athenaSays('Since this is your first time starting the app, I need to know what kind of exercise you want to do.')
    addingExercise()

time.sleep(0.25)
while 0.25:
    recordedVoice = recordVoice()
    respond(recordedVoice)


