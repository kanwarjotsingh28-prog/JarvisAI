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

        # MEMORY SAVE
        if result["intent"] == "SAVE_MEMORY":

            response = self.memory.save(command)

            result["response"] = response

            self.speaker.speak(response)

            return result

        # MEMORY RECALL
        if result["intent"] == "RECALL_MEMORY":

            value = self.memory.recall(command)

            result["response"] = value

            self.speaker.speak(value)

            return result

        # AI
        if result["destination"] == "AI Module":

            response = self.ai.ask(command)

            result["response"] = response

            self.speaker.speak(response)

            return result

        # AUTOMATION
        self.automation.execute(
            result["intent"],
            result["entity"],
            result["search_engine"],
            result["search_query"]
        )

        return result