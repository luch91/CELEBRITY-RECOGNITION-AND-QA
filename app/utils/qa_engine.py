import os
import requests

class QnAEngine:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def ask_about_celebrity(self,name,question):
        headers = {
            "Authorization": f"Bearer {self.api_key}", 
            "Content-Type": "application/json"
        }

        prompt = f"""
        You are a celebrity question-answering expert AI Assistant. You are to answer questions about {name}
        Question: {question}
        """

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
            "temperature": 0.3,
            "max_tokens": 1024
        }


        response =requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content']

        return "Sorry, I couldn't find any information about that celebrity."
