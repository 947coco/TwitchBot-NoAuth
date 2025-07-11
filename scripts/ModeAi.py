import requests


class OllamaAI():
    def __init__(self, AiName):
        self.url = "http://localhost:11434/api/generate"  # Adresse de l'API d'Ollama par défaut
        self.headers = {"Content-Type": "application/json"}
        self.AI = AiName    

    def CreatePayload(self, Message):
        return    {
       "model": self.AI,
       "prompt": Message,
       "stream": False
        }

    def SendQuestion(self, Message):
        response = requests.post(
            self.url, 
            headers=self.headers, 
            json=self.CreatePayload(Message)
            )

        if response.status_code == 200:
            data = response.json()
            print(data)
            #print(response.json()['choices'][0]['message']['content'])
        else:
            print(f"Erreur : {response.status_code}")
            print(f"Réponse : {response.text}")  # Affiche le corps de la réponse

IA = OllamaAI("qwen2.5-coder:14b")
IA.SendQuestion("Explique moi la norme ASCII et pourquoi on a changer vers UTF-8")