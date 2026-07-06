from google import genai

from backend.config.settings import Settings
from backend.memory.conversation import Conversation
from backend.ai.prompts import SYSTEM_PROMPT


class AIManager:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if hasattr(self, "_initialized"):
            return

        self.client = genai.Client(
            api_key=Settings.GEMINI_API_KEY
        )

        self.conversation = Conversation()

        self.system_prompt = SYSTEM_PROMPT

        self._initialized = True

    def ask(self, prompt, save_history=True):

        try:

            if save_history:

                self.conversation.add_user(prompt)

                history = self.system_prompt + "\n\n"

                for message in self.conversation.history():

                    history += (
                        f"{message['role']}: "
                        f"{message['content']}\n"
                    )

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=history
                )

                answer = response.text

                self.conversation.add_assistant(answer)

                return answer

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            return f"AI Error: {e}"

    def clear_history(self):

        self.conversation.clear()