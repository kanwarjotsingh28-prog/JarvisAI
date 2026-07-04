from backend.brain.brain import Brain
from backend.automation.automation import Automation
from backend.ai.ai_manager import AIManager
from backend.memory.memory_processor import MemoryProcessor
from backend.voice.speaker import Speaker


class CommandProcessor:

    def __init__(self):

        self.brain = Brain()
        self.automation = Automation()
        self.ai = AIManager()
        self.memory = MemoryProcessor()
        self.speaker = Speaker()

    def process(self, command):

        result = self.brain.think(command)

        # -------------------------
        # MEMORY : SAVE
        # -------------------------
        if result["intent"] == "SAVE_MEMORY":

            response = self.memory.save(command)

            result["response"] = response

            self.speaker.speak(response)

            return result

        # -------------------------
        # MEMORY : RECALL
        # -------------------------
        if result["intent"] == "RECALL_MEMORY":

            command_lower = command.lower()

            if "name" in command_lower:
                key = "name"

            elif "language" in command_lower:
                key = "favorite_language"

            else:
                key = None

            if key is None:

                response = "I don't know what you want me to remember."

            else:

                value = self.memory.recall(key)

                if value is None:
                    response = "I don't know that yet."
                else:
                    response = f"Your {key.replace('_', ' ')} is {value}."

            result["response"] = response

            self.speaker.speak(response)

            return result

        # -------------------------
        # AI
        # -------------------------
        if result["destination"] == "AI Module":

            response = self.ai.ask(command)

            result["response"] = response

            self.speaker.speak(response)

            return result

        # -------------------------
        # AUTOMATION
        # -------------------------
        self.automation.execute(
            result["intent"],
            result["entity"],
            result["search_engine"],
            result["search_query"]
        )

        return result