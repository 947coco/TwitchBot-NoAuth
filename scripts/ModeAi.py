# -*- coding: utf-8 -*-
import requests

class OllamaAI():
    def __init__(self, AiName: str):
        self.AI = AiName 
        self.PROMPT_DIRECTEUR = \
        "Ta réponse doit être la plus courte possible, va droit au but. Répond en français" \
        "Il t'es interdit d'utiliser des emojis et les caractères spéciaux, " \
        "tu as seulement le droit aux lettres et aux chiffres. " \
        "Le prompt est le message d'un chat twitch, tu dois fournir des " \
        "réponse divertissante, distrayante, humoristique, second degré. " \
        "Essaye d'utiliser le nom du viewer dans tes réponses."
        "Voici le message twitch et le nom du viewer. "

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
