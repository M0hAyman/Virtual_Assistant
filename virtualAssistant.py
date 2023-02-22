import speech_recognition as sr
import pyttsx3 as T2S
                                                                                                    #how ->search in chrome
                                                                                                    #open -> open application
                                                                                                    #search->get application directory
                                                                                                    #close-> close application
                                                                                                    #play-> open youtube and play
def voice1():

    engine = T2S.init()  # creating a text to speach object called "engine"
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    return engine

def listening():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ai' in command:
             print(command)

    except:
        print('error')
        pass
    return

Assistant=voice1()
Assistant.say('I am your assistant')
Assistant.say('How can I help?')
Assistant.runAndWait()
listening()

