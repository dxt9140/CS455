from pynput.keyboard import Key, Controller
import pyxhook
import time
import random
　
　
keyboard = Controller()
　
def keyDownEvent( event ):
    global running
    x = random.randint(0,15)
    #backspace previously typed character
    keyboard.press(chr(8))
　
    #type a bucnh of random chars
    for i in range(0,x):
        keyboard.press(chr(random.randint(0,127)))
    running = False
　
　
def main():
    global running
    running = True
　
    # Create PyxHook object
    keyboard_hook = pyxhook.HookManager()
　
    # keyDownEvent function is called when keydown is detected
    keyboard_hook.KeyDown = keyDownEvent
　
    # hook the keyboard to listen
    keyboard_hook.HookKeyboard()
　
    # Begin the keyboard hook thread
    keyboard_hook.start()
　
    while running:
        time.sleep(0.1)
　
    # close thread
    keyboard_hook.cancel()
　
if __name__ == '__main__':
    main()
