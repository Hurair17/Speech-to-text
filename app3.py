

# # # Importing necessary modules required 
# from playsound import playsound
# import speech_recognition as sr 
# from googletrans import Translator 
# from gtts import gTTS 
# import os


# # Capture Voice
# # takes command through microphone
# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening.....")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing.....")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"user said {query}\n")
#     except Exception as e:
#         print("say that again please.....")
#         return "None"
#     return query

# query = takecommand()
# while (query == "None"):
#     query = takecommand()
    
    
    
import translators as ts
from translate  import Translator
# LanguageChoices = {'Hindi','English','French','German','Spanish'}
# translator= Translator(from_lang="Hindi",to_lang="English")
data = 'hello aapka naam kya hai aap kaise ho'
# data = 'hello what is your name'
# translation = ts.google(data, from_language='UR', to_language='en')
from translate import Translator
translator= Translator(to_lang="ur")
translation = translator.translate(data)
# translation = translator.translate(query)
print (translation)






