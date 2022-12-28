

# importing libraries 
import speech_recognition as sr 
import pandas as pd
from googletrans import Translator

def makeCSV(text):
    com = [text]
    df = pd.DataFrame(com).transpose()
    df.to_csv('D:/JMM/10 speech to text/text.csv', mode='a', index=False, header=False)

r = sr.Recognizer()
record = True
while record:
    with sr.Microphone() as source:
        print('Recording Start.....')
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data,language='ur-in')
        print('Speech To Text : ',text)
        
        translator = Translator()
        translation = translator.translate(text)
        print ('Translated To English : ',translation.text)

        makeCSV(translation.text)
        recordAgain = input('Record other line press r else x : ') 
    #enter r to record again else close
    if recordAgain == "r":
        record = True
    if recordAgain == "x":
        record = False

        
        
        