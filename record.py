from pynput import keyboard
import pyaudio
import wave
from playsound import playsound
import speech_recognition as sr 



r = sr.Recognizer()
audio_data = 0

class recorder():
    def __init__(self):
        self.recording = False
        
    def start(self):
        print('Recording Start.....')
        with sr.Microphone() as source:
            # read the audio data from the default microphone
                #for 5 seconed duration
                # audio_data = r.record(source, duration=5)
            
            audio_data = r.record(source)

    def stop(self):
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)


    def callback(self, in_data, frame_count, time_info, status):
        self.frames.append(in_data)
        return in_data, pyaudio.paContinue

class MyListener(keyboard.Listener):
    def __init__(self):
        super(MyListener, self).__init__(self.on_press, self.on_release)
        self.recorder = recorder();

    def on_press(self, key):
        if key.char == 'r':
            self.recorder.start()
        return True

    def on_release(self, key):
        if key.char == 'r':
            self.recorder.stop();
            return True
        # Any other key ends the program
        return False

print("Press and hold the 'r' key to begin recording")
print("Release the 'r' key to end recording")

# Collect events until released
with MyListener() as listener:
    listener.join()