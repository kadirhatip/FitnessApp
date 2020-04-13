import os
os.system('cls')
import os.path
import speech_recognition as sr 
import time 
import random
import playsound
from gtts import gTTS
import openpyxl
from openpyxl import load_workbook
from string import ascii_uppercase



rec = sr.Recognizer()
dateiName = "trainingsDaten.xlsx"

def erstnutzungPrüfen(_dateiName):

    if os.path.isfile(dateiName):
        athenaSagt('Willkommen zurück. Wollen wir wieder trainieren?')
    else:
        neueExcelTabelleErstellen(dateiName)
        athenaSagt('Willkommen zur fitness app. Mein Name ist Athena, und ich werde dein Training begleiten.')
        athenaSagt('Da du die App anscheinend zum ersten mal startest, muss ich wissen welche Übungen und wie viele Sätze du mit wie vielen Wiederholungen machen willst')
        athenaSagt('Schaue dazu, auf dein Gerät, und füge Übungen hinzu.')


def nutzerSagt():

    with sr.Microphone() as source:

        vInput = rec.listen(source)

        try: 
            vOutput = rec.recognize_google(vInput, language='de_DE')
        except sr.UnknownValueError:
            athenaSagt('Sorry, das habe ich nicht verstanden')
        except sr.RequestError:
            athenaSagt('Sorry, ich kann momentan auf den sprach service nicht zugreifen.')
        return vOutput


def athenaAntwortet(vInput):
    if 'starte training' in vInput:
        athenaSagt('Ok, starte die Fitness App')    
    elif 'jo' in vInput:
        athenaSagt('Ok, starte die Fitness App')
    elif 'beenden' in vInput:
        athenaSagt('Alles klar. Bis zum nächsten mal.')
        exit()


def athenaSagt(audioString):
    tts = gTTS(text=audioString, lang='de')
    r = random.randint(1,10000000)
    audioFile = 'audio-' + str(r) + '.mp3'
    tts.save(audioFile)
    print(audioString)
    playsound.playsound(audioFile)
    os.remove(audioFile)

def okAthena():
    pass 


def neueExcelTabelleErstellen(_dateiName):
    #Leeren Workbook erstellen
    wb = openpyxl.Workbook()

    #Sheet für Übungen und Fortschritt erstellen
    übungsSheet = wb.active
    übungsSheet.title = 'Uebungen'
    datenSheet = wb.create_sheet('Trainingsdaten')

    #Beim erstmaligen Erstellen des Excels noch nur ges. Wiederholungen. Beim Verarbeiten durch Athena müssen dann noch die einzelnen Wiederholungen der Sätze dazukommen.
    headerÜbungsSheet = ['Uebung', 'Saetze', 'Wiederholungen', 'Beschreibung']
    headerDatenSheet = ['Datum', 'Uebung', 'Saetze', 'Gesamte Wiederholungen']    

    # Überschriften in die oberste Zeile der Exceltabelle eintragen
    for i in range(0, len(headerÜbungsSheet)):
        übungsSheet[str(ascii_uppercase[i]) + str(1)] = headerÜbungsSheet[i]
    
    for i in range(0, len(headerDatenSheet)):
        datenSheet[str(ascii_uppercase[i]) + str(1)] = headerDatenSheet[i]

    #Workbook abspeichern
    wb.save(filename=_dateiName)

def übungHinzufügen(_dateiName, _übung, _sets, _reps, _beschreibung):
    #excel übungsSheet öffnen
    wb = load_workbook(filename = _dateiName)
    sheet = wb.active
    #checken welches column noch nicht eingetragen wurde

    #auf das nächste freie column die attribute eintragen
    liste = [_übung, _sets, _reps, _beschreibung]
    sheet.append(liste)
    #excel speichern
    wb.save(filename= _dateiName)

def löscheWorkbook(titleOfWorkbook):
    os.remove(titleOfWorkbook)

def starteTraining():
    pass


    
erstnutzungPrüfen(dateiName)
okAthena()

time.sleep(0.25)
while 0.25:
    nutzerStimme = nutzerSagt()
    athenaAntwortet(nutzerStimme)


