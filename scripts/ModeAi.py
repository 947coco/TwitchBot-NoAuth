import requests
import json

class OllamaAI():
    def __init__(self, AiName):
        self.url = "http://localhost:11434/api/generate"  # Adresse de l'API d'Ollama par défaut
        self.headers = {"Content-Type": "application/json"}
        self.AI = AiName    

    def CreatePayload(self, Message):
        self.payload = {
            "model": self.AI,  # Modèle utilisé
            "messages": [
                {
                    "role": "user",
                    "content": "Raconte-moi une bonne blague"
                }
            ],
            "temperature": 0.7,   # Niveau de créativité (entre 0 et 1)
            "max_tokens": 500     # Limite du nombre de tokens dans la réponse
        }

    def SendQuestion(self, Message):
        response = requests.post(self.url, headers=self.headers, json=self.CreatePayload(Message))

        if response.status_code == 200:
            print(response.json())
            print(response.json()['choices'][0]['message']['content'])
        else:
            print(f"Erreur : {response.status_code}")

IA = OllamaAI("deepseek-r1:14b")
IA.SendQuestion("Bonjour, comment vas-tu ?")