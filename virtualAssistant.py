import speech_recognition as sr
import pyttsx3 as T2S
import os
import subprocess  # how ->search in chrome
import webbrowser

# open -> open application
All_EXE_lnk_Directories = []
BS = '\\'

def found(found):
    if(not found):
        print('Did not found what you are looking For')
        say('Did not found what you are looking For')
    else:
        say('here is what I found')


def search(word, assistant):  #chatGPT or local disk or chrome
    flag = False

    for path in All_EXE_lnk_Directories:
        sub_directories = path.split("\\")
        if word in sub_directories[-1].lower():  # priority 2
            print(path)
            flag = True
    return flag

def search_for_open(word, assistant):  #chatGPT or local disk or chrome
    flag = False
    for path in All_EXE_lnk_Directories:
        sub_directories=path.split("\\")
        if word==sub_directories[-1].lower():        # priority 1
            catch_path = path
            flag = True
            return catch_path

    for path in All_EXE_lnk_Directories:
        sub_directories = path.split("\\")
        if word in sub_directories[-1].lower():     # priority 2
            catch_path = path
            flag = True
            return catch_path

    for path in All_EXE_lnk_Directories:            # last priority
        if word in path.lower():
            catch_path = path
            flag = True
            return catch_path

    return flag

def openApp(app, assistant):  # Tested apps passed: chrome,vlc,teams,notion,notepad
    # Tested apps failed: Discord,word, powerpoint (due to . and diffrent exe file names) ..To be handled later
    """"

    -Open criteria: "(name of file to be opened).exe" if not found it won't work
    -Some cases like teams there are many teams.exe (i dont know why) files it
     will take the last one searched and it works in my pc(needs to be tested with other pc)

    """
    exe_path = app + '.exe'
    lnk_path= app+'.lnk'
    exe = False
    lnk = False
    print('searching for ' + app + ' to be opened......')
    say('searching for ' + app + ' to be opened......')

    path = search_for_open(lnk_path, assistant)
    if(path):
        print('printing path (lnk path)... ')
        print(path)
        lnk = True
    elif(search_for_open(exe_path, assistant)):
        path = search_for_open(exe_path, assistant)
        print('printing path (exe path)... ')
        print(path)
        exe = True
    else:
        found(False)
        return

    try:
            print('opening ' + app + '......')
            say('Found successfully .. opening ' + app)
            if (exe):
                subprocess.call(path)
            elif (lnk):
                os.startfile(path)
    except:
            print('could not open file')


def Actions(command, assistant):
    command = str(command).split()
    try:
        if ('chat gpt' in command) or ("chat gbt" in command) or ("gpt" in command) or ("gbt" in command):
            webbrowser.open("https://poe.com/ChatGPT")

        elif 'how' in command:
            query = " ".join(command)  # Join all the words
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)

        elif 'play' in command:
            # What_to_play=command.split('play')[-1]
            # # query = " ".join(What_to_play)
            # url = f"https://www.youtube.com/results?search_query={lstrip(What_to_play)}"
            # webbrowser.open(url)
            query = "".join(command[1:])  # Join all the words except the first one
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
        elif 'find' in command:
            # searching_for = command[command.index('find') + 1]
            searching_for = command[-1]

            print('finding ' + searching_for + ' ......')
            say('finding ' + searching_for + ' ......')
            found(search(searching_for, assistant))

        elif 'search' in command:
            # searching_for = command[command.index('search') + 2]
            searching_for = command[-1]
            print('searching for ' + searching_for + ' ......')
            say('searching for ' + searching_for + ' ......')

            found(search(searching_for, assistant))
        elif 'where' in command:

            searching_for = command[-1]
            print('searching for ' + searching_for + ' ......')
            say('searching for ' + searching_for + ' ......')

            found(search(searching_for, assistant))

        elif 'open' in command:
            # app_name = command[command.index('open') + 1]
            app_name = command[-1]
            say('Please confirm by saying yes, Are you sure you want to open ' + app_name)
            ans = listening()
            if 'yes' in ans:
                openApp(app_name, assistant)
            else:
                say("Confirmation failed repeat what you said again")




        else:
            # print("Else innn")
            say('did not understand command')
    except:
        say('did not understand command and error happened')
        # print("went in actions exception")


# def show(List):
#     for ele in List:
#         if ".lnk" in ele:
#             print(ele)
#     # print(len(List))


def listDir(dir):  # Recusive fn to get the path of every executable file on the PC and append it to All_EXE_Directories List
    try:
            filenames = os.listdir(dir)
            # print(filenames)
            for file in filenames:
                path2 = dir + BS + file
                # print(path2)
                # print("file path: " + os.path.abspath(os.path.join(dir, file)) + "\n")  # displays the real directory without double back salashes
                if '.exe' in path2:
                    if (str(path2)[-1] == 'e' and str(path2)[-2] == 'x' and str(path2)[-3] == 'e'):
                        real_path = os.path.abspath(os.path.join(dir, file))
                        All_EXE_lnk_Directories.append(real_path)
                if '.lnk' in path2:
                    if (str(path2)[-1] == 'k' and str(path2)[-2] == 'n' and str(path2)[-3] == 'l'):
                        real_path = os.path.abspath(os.path.join(dir, file))
                        All_EXE_lnk_Directories.append(real_path)

                listDir(path2)
    except:
        # print('error in listDir')
        pass  # for future reference: pass is only a placeholder that removes errors until a code is written


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
        # say('error in listening, I did not hear what you said correctly')
    return


Assistant = voice1()


def say(command):
    Assistant.say(command)
    Assistant.runAndWait()


def main():
    # l="C:\\Users\Hp\Downloads\Team_1_Report (1).pdf".split('\\')
    # print(l)
    listDir('C:\\')
    listDir('D:\\')
    say('Hello, I am your Windows assistant')
    say('How can I help?')
    # while(True):
    #     Command = listening()
    #     if ("hey windows" in Command):
    #         Actions(Command, Assistant)

    while (True):
        Command = listening()
        Actions(Command, Assistant)




if __name__ == "__main__":  # This line is useless here but good practice
    main()


