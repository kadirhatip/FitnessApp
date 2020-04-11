import os
os.system('cls')

import speech_recognition as sr 

rec = sr.Recognizer()

def recordVoice():

    with sr.Microphone() as source:

        vInput = rec.listen(source)

        try: 
            vOutput = rec.recognize_google(vInput)
        except sr.UnknownValueError:
            print('Sorry Boss, I did not get that')
        except sr.RequestError:
            print('Sorry Boss, my speech service seems to be down right now')
        return vOutput

def respond(vInput):
    if 'start training' in vInput:
        print('Ok Boss, starting Fitness App')
        fitnessApp()

def fitnessApp():
    pass



print('How can I help you Boss')
recordedVoice = recordVoice()

respond(recordedVoice)