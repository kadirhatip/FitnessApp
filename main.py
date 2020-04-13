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
            vOutput = rec.recognize_google(vInput, language='de_DE')
        except sr.UnknownValueError:
            athenaSays('Sorry, das habe ich nicht verstanden')
        except sr.RequestError:
            athenaSays('Sorry, ich kann momentan auf den sprach service nicht zugreifen.')
        return vOutput


#Processing Userinput.
def respond(vInput):
    if 'starte training' in vInput:
        athenaSays('Ok, starte die Fitness App')    
    elif 'jo' in vInput:
        athenaSays('Ok, starte die Fitness App')
    elif 'beenden' in vInput:
        athenaSays('Alles klar. Bis zum nächsten mal.')
        exit()

#Playing audio through text-to-speech
def athenaSays(audioString):
    tts = gTTS(text=audioString, lang='de')
    r = random.randint(1,10000000)
    audioFile = 'audio-' + str(r) + '.mp3'
    tts.save(audioFile)
    print(audioString)
    playsound.playsound(audioFile)
    os.remove(audioFile)

def addingExercise():
    pass

def deletingWorkbook(titleOfWorkbook):
    os.remove(titleOfWorkbook)

def fitnessApp():
    pass




if os.path.isfile('trainingsDaten.xlsx'):
    athenaSays('Willkommen zurück. Wollen wir wieder trainieren?')
else:
    wb = openpyxl.Workbook()
    wb.save('trainingsDaten.xlsx')
    athenaSays('Willkommen zur fitness app. Mein Name ist Athena, und ich werde dein Training begleiten.')
    athenaSays('Da du die App anscheinend zum ersten mal startest, muss ich wissen welche Übungen und wie viele Sätze du mit wie vielen Wiederholungen machen willst')
    athenaSays('Schaue dazu, auf dein Gerät')
    addingExercise()

time.sleep(0.25)
while 0.25:
    recordedVoice = recordVoice()
    respond(recordedVoice)


