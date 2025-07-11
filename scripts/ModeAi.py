# -*- coding: utf-8 -*-
import requests

class OllamaAI():
    def __init__(self, AiName: str):
        self.AI = AiName  

    def SendQuestion(self, Message:str, NomViewer: str):        
        response = requests.post(
            url = "http://localhost:11434/api/generate",  # Adresse de l'API d'Ollama par défaut 
            headers = {"Content-Type": "application/json"}, # Format de la requete
            json = { 
                    "model": self.AI,
                    "prompt": Message,
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
IA.SendQuestion("Explique moi la norme ASCII et pourquoi on a changer vers UTF-8", "Jambon_Beurre83")