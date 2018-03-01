"""
Authors:
    Dominick Taylor (dxt9140@g.rit.edu)
    Bikash
    Isza

Created: 2/28/2018

A simple keylogger file that captures user key events using the pyxhook package.
Note, this is NOT intended as a malicious program. It is used to understand
security principles and demonstrate mastery of secure programming techniques.
"""

import pyxhook
import time

def kbevent( event ):
    global running

    if event.Ascii == 32:
        # Spacebar indicates to end the program
        running = False
    
    print("Key pressed")

"""
Instantiate an instance of the HookManager class. This is the main class used
by the pyxhook library to capture and interpret key presses.
"""
keyboard_hook = pyxhook.HookManager()

"""
Specify the function to call whenever a key is pressed.
"""
keyboard_hook.KeyDown = kbevent

"""
This is the command used to specify that the HookManager should begin listening
to the keyboard.
"""
keyboard_hook.HookKeyboard()

"""
The HookManager class runs as a separate thread as defined in the standard
threading library. Calling start runs the program as a separate thread.
"""
keyboard_hook.start()

running = True
while running:
    time.sleep( 0.1 )

"""
Once the spacebar has been pressed and running set to false, the program should
quit.
"""
keyboard_hook.cancel()

#------------------------------------
# End of file

