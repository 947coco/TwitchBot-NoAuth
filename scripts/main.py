import subprocess
import platform
import threading
import time
import re

if platform.system() == "Linux": 
    subprocess.run("sudo apt install espeak ffmpeg libespeak1")

from VariablesCheck import *
from TwitchConnection import *
from TexteToSpeech import *

File = Variables("config.txt")
USERNAME, BANWORDS, DELAIS, FORMAT, SHORTCUT = File.GetVariables()

Voice = TTS()

Twitch = Connection(USERNAME)
Twitch.ConnectionTwitchChat()

PingCheck = threading.Thread(target=Twitch.HandlePingVerification)
PingCheck.daemon = True
PingCheck.start()


while True:
    ViewerName, ViewerMessage = Twitch.ProcessMessage() 
    if ViewerName == 0 or ViewerMessage == 0: continue
    Reponse = Twitch.FormatUserMessage(ViewerName, ViewerMessage, FORMAT)
    if len(Reponse) > 150: continue
    for mot in BANWORDS:
        if mot in Reponse: Reponse = Reponse.replace(mot, " ")
    char_speciaux = [":", "&", "~", "#", "@", "^", "_", ".", "[", "]", "{", "}", "=", "+", "-", "*", "!", "/", ";" ",", "?"]
    for char in char_speciaux:
        Reponse = Reponse.replace(char, " ")
    Reponse = re.sub(r'[^\w\s]', '', Reponse)
    print(Reponse)
    Voice.Dit(Reponse)

    time.sleep(float(DELAIS))


