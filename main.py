import os
os.system('cls')

import speech_recognition as srg 

rec = srg.Recognizer()

with srg.Microphone() as source:

    print('Lets test pyaudio, speak now!')

    paudio = rec.listen(source)

    print('Ok!')

    print('Test voice to text: \n' + rec.recognize_google(paudio)) 