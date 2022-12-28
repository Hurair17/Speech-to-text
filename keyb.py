import keyboard
import speech_recognition as sr 


r = sr.Recognizer()
x = True
# while x:
#     print('Recording Start.....')

with sr.Microphone() as source:
# read the audio data from the default microphone
    #for 5 seconed duration
    audio_data = r.record(source)
    # print('x to close recording')
    
    text = r.recognize_google(audio_data)
    print(text)
        # if keyboard.is_pressed("x"):
        #     text = r.recognize_google(audio_data)
        #     print(text)
        #     x = False
        