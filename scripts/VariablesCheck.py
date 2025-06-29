# -*- coding: utf-8 -*-
class Variables():
    def __init__(self, file: str):
        with open(file, 'r', encoding='utf-8') as file:
            self.raw = file.readlines()

    def FindContent(self, ligne: str):
        indexs = []
        for i, char in enumerate(ligne):
            if char == '"': indexs.append(i)
        return ligne[indexs[0]+1:indexs[1]]

    def GetVariables(self):
        for line in self.raw:
            if "PseudoTwitch" in line: USERNAME = self.FindContent(line)
            if "MotsBannis" in line: BANWORDS = self.FindContent(line).split(" ")
            if "DélaisVérification" in line: DELAIS = self.FindContent(line)
            if "FormatRéponse" in line: FORMAT = self.FindContent(line)
            if "RaccourciToutArrêter" in line: SHORTCUT = self.FindContent(line)
            if "IaChoisi" in line: AI = self.FindContent(line)

        if '' in BANWORDS: BANWORDS.remove('')
        if ' ' in BANWORDS: BANWORDS.remove(' ')

        MessageErreurUSERNAME = "Aucun pseudo twitch n'a été détécté, merci de modifier le fichier config.txt"
        MessageErreurSHORTCUT = "Le raccourci clavier doit contenir Ctrl, Alt ou Shif, merci de modifier le fichier config.txt"
        assert len(USERNAME) > 0 , MessageErreurUSERNAME
        assert "ctrl" in SHORTCUT or "alt" in SHORTCUT or "shift" in SHORTCUT, MessageErreurSHORTCUT
        
        return USERNAME, BANWORDS,  DELAIS, FORMAT, SHORTCUT
