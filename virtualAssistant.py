import speech_recognition as sr
import pyttsx3


listener=sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')
# print(voices[1].id)
#print(voices[0])
#print(voices[1])
engine.setProperty('voices', voices[0].id)

engine.say('I am your assistant')
engine.say('How can I help?')
engine.runAndWait()
try:
  with sr.Microphone() as source:
    print('listening...')
    voice =listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()
    if 'alexa' in command:
        print(command) 

except:
  print('error')
  pass


