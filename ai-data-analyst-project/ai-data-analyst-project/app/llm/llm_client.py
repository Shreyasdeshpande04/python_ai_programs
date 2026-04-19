import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class LlamaClient:
    def __init__(self):
        # This uses the Llama3 model on the cloud (0GB local space)
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile"

    def get_ai_response(self, prompt: str):
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
        )
        return chat_completion.choices[0].message.content