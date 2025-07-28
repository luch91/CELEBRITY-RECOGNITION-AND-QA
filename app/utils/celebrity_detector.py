import os
import base64
import requests


class CelebrityDetector:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def identify(self, image_bytes):
        encoded_image = base64.b64encode(image_bytes).decode()

        headers = {
            "Authorization": f"Bearer {self.api_key}", 
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "You're a celebrity detection and question-answering expert AI.\n"
                                "Identify the celebrity in the image. If known, respond in this format:\n"
                                "- **Full Name**:\n"
                                "- **Profession**:\n"
                                "- **Famous For**:\n"
                                "- **Top Achievements**:\n\n"
                                "If the celebrity is not known, respond with \"Unknown\"."
                            )
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        }
                    ]
                }
            ],
            "temperature": 0.3,
            "max_tokens": 1024
        }

        response = requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content']
            name = self.extract_name(result)
            return result, name

        return "Unknown", ""

    def extract_name(self, content):
        for line in content.splitlines():
            if line.lower().startswith("- **full name**:"):
                return line.split(":", 1)[1].strip()