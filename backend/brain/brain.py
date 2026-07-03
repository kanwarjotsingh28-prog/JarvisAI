from backend.brain.intent_detector import IntentDetector
from backend.brain.command_router import CommandRouter
from backend.brain.entity_extractor import EntityExtractor


class Brain:

    def __init__(self):
        self.detector = IntentDetector()
        self.router = CommandRouter()
        self.extractor = EntityExtractor()

    def think(self, command):

        intent = self.detector.detect(command)

        destination = self.router.route(intent)

        entity = self.extractor.extract(command)

        return {
            "command": command,
            "intent": intent,
            "entity": entity,
            "destination": destination
        }