import keyboard
import time

def key_press(text):
    text = text.split(" ") # split the text into a list of words
    for i in text:
        if i == "jump":
            keyboard.press("Space")
            time.sleep(0.05) # wait 50 milliseconds, space has a press threshold
            keyboard.release("Space")
        elif i == "sneak": 
            keyboard.press("Shift")
            keyboard.release("Shift")
        elif i == "sprint":
            keyboard.press("Ctrl")
        elif i == "left":
            keyboard.press("a")
        elif i == "right":
            keyboard.press("d")
        elif i == "back": 
            keyboard.press("s")
        elif i == "move": 
            keyboard.press("w")
        elif i == "drop":
            keyboard.press("q")
            keyboard.release("q")
        elif i == "inventory": 
            keyboard.press("e")
            keyboard.release("e")
        elif i == "swap":
            keyboard.press("f")
            keyboard.release("f")
        elif i == "players":
            keyboard.press("tab")
        elif i == "close":
            keyboard.release("tab")
        elif i == "stop":
            keyboard.release("w")
            keyboard.release("a")
            keyboard.release("s")
            keyboard.release("d")
            keyboard.release("Ctrl")