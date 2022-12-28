

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
        # read the audio data from the default microphone
        #for 5 seconed duration
        # audio_data = r.record(source, duration=5)
        # print('Wait .....') 
        #Adjust noise thresould according to the sournding
        # r.adjust_for_ambient_noise(source, duration=2)
		#listens for the user's input
        # audio_data = r.listen(source)
  
        print('Recording Start.....')
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        
        # convert speech to text
        text = r.recognize_google(audio_data,language='ur-in')
        print('Speech To Text : ',text)
        
        
        
        #For Translation
        from translate import Translator
        translator= Translator(from_lang = 'ur',to_lang="en")
        translation = translator.translate(text)
        # translation = translator.translate(query)
        print ('Translated To English : ',translation)
        
        
        
        
        

        makeCSV(translation)
        recordAgain = input('Record other line press r else x : ') 
    #enter r to record again else close
    if recordAgain == "r":
        record = True
    if recordAgain == "x":
        record = False

        
        
        