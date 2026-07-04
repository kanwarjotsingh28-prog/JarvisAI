from google import genai
from backend.config.settings import Settings
from backend.memory.conversation import Conversation


class AIManager:

    def __init__(self):

        self.client = genai.Client(
            api_key=Settings.GEMINI_API_KEY
        )
        self.conversation = Conversation()

    def ask(self, prompt):

        try:

            self.conversation.add_user(prompt)

            history = ""

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

        except Exception as e:

            return f"AI Error: {e}"