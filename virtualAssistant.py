import speech_recognition as sr
import pyttsx3 as T2S
import os                                                                                                    #how ->search in chrome
                                                                                                             #open -> open application
All_EXE_Directories = []
BS = '\\'

def search(word,assistant):
    flag=False
    listDir('C:\\')
    listDir('D:\\')
    for path in All_EXE_Directories:
        if word in path.lower():
            print(path)
            flag=True
    if flag==False:
        assistant.say('Did not found what you are looking For')

def Actions(command,assistant):
    command = str(command).split()
    try:
        if 'find' in command:                                      #3ayzeen ne7el moshkelet el kelma el feha gomleten
            searching_for = command[command.index('find')+1]
            search(searching_for,assistant)
        elif 'search' in command:
            searching_for = command[command.index('search')+2]
            search(searching_for,assistant)
        elif 'play' in command:
            #Insert your code here
            pass #delete this

        elif 'how' in command:
            #Insert your code here
            pass #delete this
        else:
            assistant.say('did not understand command')

    except:
        assistant.say('did not understand command')

def show(List):
    for ele in List:
        print(ele)
    print(len(List))

def listDir(dir):
    try:
        if '.' in dir:
            return
        else:
            filenames = os.listdir(dir)
            # print(filenames)
            for file in filenames:
                path2 = dir + BS + file
                # print(path2)
                # print("file path: " + os.path.abspath(os.path.join(dir, file)) + "\n")  # displays the real directory without double back salashes
                if '.exe' in path2 :
                    if (str(path2)[-1]=='e' and str(path2)[-2]=='x' and str(path2)[-3]=='e'):
                        real_path = os.path.abspath(os.path.join(dir, file))
                        All_EXE_Directories.append(real_path)

                listDir(path2)
    except:
        # print('error')
        pass




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
            print(command)
            return command

    except:
        print('error')
        pass
    return

Assistant = voice1()
Assistant.say('I am your assistant')
Assistant.say('How can I help?')
Assistant.runAndWait()
Command = listening()
Actions(Command,Assistant)
print(type(Command))


