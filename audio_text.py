import speech_recognition as sr 
from googletrans import Translator


r = sr.Recognizer()

# filename = 'D:/JMM/10 speech to text/RE1d2b33be62e901058173ffd8e5a9ff80.wav'

filename = 'D:/JMM/10 speech to text/RE8dc7f6318b81596e65a53f8fb890ba86.wav'
with sr.AudioFile(filename) as source:
    print('Recording Start.....')
    audio_data = r.record(source)
    print("Recognizing...")
    # convert speech to text
    # text = r.recognize_google(audio_data,language='ur-in')
    text = r.recognize_google(audio_data)
    
    print('Speech To Text : ',text)
    
    translator = Translator()
    translation = translator.translate(text)
    print ('Translated To English : ',translation.text)