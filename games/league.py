import keyboard

def key_press(text):
    text = text.split(" ") # split the text into a list of words
    for i in text:
        if i == "one":
            keyboard.press("q")
            keyboard.release("q")
        elif i == "two":
            keyboard.press("w")
            keyboard.release("w")
        elif i == "three":
            keyboard.press("e")
            keyboard.release("e")
        elif i == "four":
            keyboard.press("t") # I use this to ult, you can change it to whatever you want
            keyboard.release("t")
        elif i == "five":
            keyboard.press("d")
            keyboard.release("d")
        elif i == "six":
            keyboard.press("f")
            keyboard.release("f")
        elif i == "shop":
            keyboard.press("p")
            keyboard.release("p")
