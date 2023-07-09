import speech_recognition as sr
from dotenv import load_dotenv
import threading
import time
import os
import sys

# to change the game, change the import statement below
from games.minecraft import key_press

def recognize_speech():
    try:
        init_rec = sr.Recognizer()
        global api_key # grab the API key from the global variable
        with sr.Microphone() as source:
            audio_data = init_rec.record(source, duration = 1.25) # record for 1 second
            text = init_rec.recognize_wit(audio_data, key=api_key).lower() # recognize the speech using Wit.ai
            key_press(text) # call the key_press function from the selected game
            # print(text) # used to see output for validation
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Request error: {e}")

load_dotenv() # load the .env file
api_key = os.getenv("API_KEY") # grab the API key from the .env file

# Create two threads for speech recognition
threads = []
for _ in range(2):
    thread = threading.Thread(target=recognize_speech) # create a thread
    threads.append(thread) # add the thread to the list of threads

# Start the threads at 1 second intervals
while True:
    try:
        for thread in threads:
            thread = threading.Thread(target=recognize_speech) 
            thread.start() # start the thread
            time.sleep(1.25) # wait 1 second before starting the next thread
        # Wait for all threads to finish
        for thread in threads:
            if thread.is_alive():
                thread.join()
    except KeyboardInterrupt:
        sys.exit(0) 
