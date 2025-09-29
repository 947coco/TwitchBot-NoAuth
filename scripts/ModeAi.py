# -*- coding: utf-8 -*-
import requests

class OllamaAI():
    def __init__(self, AiName: str):
        self.AI = AiName 
        self.PROMPT_DIRECTEUR = \
        "You must summarize this message from a Twitch chat." \
        "The result must not exceed 50 characters."

    def SendQuestion(self, Message:str, NomViewer: str):        
        response = requests.post(
            url = "http://localhost:11434/api/generate",  # Adresse de l'API d'Ollama par défaut 
            headers = {"Content-Type": "application/json"}, # Format de la requete
            json = { 
                    "model": self.AI,
                    "prompt" : self.PROMPT_DIRECTEUR + NomViewer + " a dit : " + Message,
                    "stream": False,
                    "session": NomViewer
                } 
            )
                    
        if response.status_code == 200:
            data = response.json()
            print(data["response"])
        else:
            raise RuntimeError(f"La réponse n'as pas été reçu, code d'erreur :{response.status_code}")

IA = OllamaAI("orca-mini:3b")
IA.SendQuestion("Quel est la meilleur carte dans clash royal ?", "Jambon_Beurre83")
