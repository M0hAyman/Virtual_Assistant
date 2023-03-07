import speech_recognition as sr
import pyttsx3 as T2S
import os
import subprocess                                                                                                    #how ->search in chrome
                                                                                                             #open -> open application
All_EXE_Directories = []
BS = '\\'

def search(word,assistant):
    flag=False
    listDir('C:\\')
    listDir('D:\\')
    for path in All_EXE_Directories:
        if word in path.lower():
            #print("in search")
            print(path)
            catch_path=path
            flag=True
    if flag==False:
        say('Did not found what you are looking For')
        return flag
    else:
        return catch_path

def openApp(app,assistant): #Tested apps passed: chrome,vlc,teams,notion,notepad
                            #Tested apps failed: Discord,word, powerpoint (due to . and diffrent exe file names) ..To be handled later
    """"
    
    -Open criteria: "(name of file to be opened).exe" if not found it won't work
    -Some cases like teams there are many teams.exe (i dont know why) files it  
     will take the last one searched and it works in my pc(needs to be tested with other pc)
    
    """
    app_end_path='\\'+ app + '.exe' 
    print('searching for '+app+' to be opened......')
    say('searching for '+app+' to be opened......')
    if(search(app_end_path, assistant) ==False):
        print('File not found and will not be opened')
        say('File not found and will not be opened')
    else:
        path=search(app_end_path, assistant)
        print('printing path... printed in open')
        print(path)
        try:
            print('opening '+app+'......')
            say('Found successfully .. opening '+app)
            subprocess.call(path)
        except:
            print('could not open file')


def Actions(command,assistant):
    command = str(command).split()
    try:
        if 'find' in command:                                      #3ayzeen ne7el moshkelet el kelma el feha gomleten
            searching_for = command[command.index('find')+1]
            print('finding '+searching_for+' ......')
            say('finding '+searching_for+' ......')
            search(searching_for,assistant)
        elif 'search' in command: #problem to be solved: if a folder has a . in its name it will not get the .exe files inside it for ex)discord files
            searching_for = command[command.index('search')+2]
            print('searching for '+searching_for+' ......')
            say('searching for '+searching_for+' ......')

            search(searching_for,assistant)
        elif 'open' in command: 
            app_name=command[command.index('open')+1]
            say('Please confirm by saying yes, Are you sure you want to open '+app_name)
            ans=listening()
            if ans=="yes":
                openApp(app_name,assistant)
            else:
                say("Confirmation failed repeat what you said again")
            
        elif 'play' in command:
            #Insert your code here
            pass #delete this

        elif 'how' in command:
            #Insert your code here
            pass #delete this
        else:
            #print("Else innn")
            say('did not understand command')
    except:
        say('did not understand command and error happened')
        #print("went in actions exception")

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
        #print('error in listDir')
        pass #for future reference: pass is only a placeholder that removes errors until a code is written



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
        print('error in listening')
        say('error in listening, I did not hear what you said correctly')
    return

Assistant = voice1()
def say(command):
    Assistant.say(command)
    Assistant.runAndWait()


def main():
    say('Hello, I am your assistant')
    say('How can I help?')
    Command = listening()
    Actions(Command,Assistant)
    print(type(Command))

if __name__ == "__main__": #This line is useless here but good practice 
	main()



