# -*- coding: utf-8 -*-
import pyttsx3

class TTS:
    def __init__(self):
        self.robot = pyttsx3.init()

    def Say(self, message: str):
        self.robot.say(message)
        self.robot.runAndWait()
