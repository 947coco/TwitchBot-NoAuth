# -*- coding: utf-8 -*-
class Variables():
    def __init__(self, file: str):
        with open(file, 'r', encoding='utf-8') as file:
            self.raw = file.readlines()

    def FindContent(self, ligne: str):
        """Return the variable between quotes"""
        indexs = []
        for i, char in enumerate(ligne):
            if char == '"': indexs.append(i)
        return ligne[indexs[0]+1:indexs[1]]

    def GetVariables(self):
        word = ""
        for line in self.raw:
            if "Twitch username" in line: USERNAME = self.FindContent(line)
            elif "Delay check" in line: DELAY = self.FindContent(line)
            elif "Ban words" in line: BANWORDS = self.FindContent(line).split(" ")
            elif "Anwser format" in line: FORMAT = self.FindContent(line)
            elif "Shortcut to stop everything" in line: SHORTCUT = self.FindContent(line)
            elif "Number of caracters max" in line: CHAR_MAX = self.FindContent(line)

        if '' in BANWORDS: BANWORDS.remove('')
        if ' ' in BANWORDS: BANWORDS.remove(' ')

        ERROR_USERNAME = "Aucun pseudo twitch n'a été détécté, merci de modifier le fichier config.txt"
        ERROR_SHORTCUT = "Le raccourci clavier doit contenir Ctrl, Alt ou Shif, merci de modifier le fichier config.txt"
        assert len(USERNAME) > 0 , ERROR_USERNAME
        assert any(key in SHORTCUT for key in ("ctrl", "alt", "shift")), ERROR_SHORTCUT
        
        return USERNAME, BANWORDS, DELAY, FORMAT, SHORTCUT, CHAR_MAX
