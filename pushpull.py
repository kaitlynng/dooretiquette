from flask import Flask
from flask_ngrok import run_with_ngrok
from playsound import playsound
from pathlib import Path
import os
import random

app = Flask(__name__)
run_with_ngrok(app) #starts ngrok when app is run

soundPlaying = False

@app.route("/", methods=["POST", "GET"])

def hello_world():
    global soundPlaying
    if soundPlaying == False:
        soundPlaying = True
        songFile = getSong()
        playsound(songFile)
        soundPlaying = False
    return songFile

def getSong():
    soundFolder = Path('C:/Users/Hui Ling/Music/voicelinesforPP/')
    songName = random.choice(os.listdir(soundFolder))
    songFile = 'C:/Users/Hui Ling/Music/voicelinesforPP/' + songName
    print(songFile)
    return songFile

if __name__ == '__main__':
    app.run()
