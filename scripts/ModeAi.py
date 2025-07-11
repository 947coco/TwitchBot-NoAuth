# -*- coding: utf-8 -*-
import requests
import time
class OllamaAI():
    def __init__(self, AiName: str):
        self.AI = AiName 
        self.PROMPT_DIRECTEUR = "Ta réponse doit contenir au maximum 160 caractères" \
        "sans caractères spéciaux, juste avec des lettres et/ou des chiffres." \
        "Le prompt suivant est un message twitch, le spectateur te posant cette question " \
        "souhaite une réponse divertissante et distrayante. Voici sa question : "

    def SendQuestion(self, Message:str, NomViewer: str):        
        response = requests.post(
            url = "http://localhost:11434/api/generate",  # Adresse de l'API d'Ollama par défaut 
            headers = {"Content-Type": "application/json"}, # Format de la requete
            json = { 
                    "model": self.AI,
                    "prompt": self.PROMPT_DIRECTEUR + Message,
                    "stream": False,
                    "session": NomViewer
                } 
            )
                    
        if response.status_code == 200:
            data = response.json()
            print(data["response"])
        else:
            raise RuntimeError(f"La réponse n'as pas été reçu, code d'erreur :{response.status_code}")

IA = OllamaAI("qwen2.5-coder:14b")
IA.SendQuestion("Qui est arrivé en 1er, l'oeuf ou la poule ?", "Jambon_Beurre83")
