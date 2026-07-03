from backend.brain.brain import Brain
from backend.automation.automation import Automation
from backend.ai.ai_manager import AIManager


class CommandProcessor:

    def __init__(self):

        self.brain = Brain()
        self.automation = Automation()
        self.ai = AIManager()

    def process(self, command):

        result = self.brain.think(command)

        if result["destination"] == "AI Module":

            result["response"] = self.ai.ask(command)

            return result

        self.automation.execute(
            result["intent"],
            result["entity"],
            result["search_engine"],
            result["search_query"]
        )

        return result