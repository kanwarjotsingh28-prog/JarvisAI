from backend.brain.intent_detector import IntentDetector
from backend.brain.command_router import CommandRouter
from backend.brain.entity_extractor import EntityExtractor
from backend.brain.search_parser import SearchParser


class Brain:

    def __init__(self):
        self.detector = IntentDetector()
        self.router = CommandRouter()
        self.extractor = EntityExtractor()
        self.search_parser = SearchParser()

    def think(self, command):

        intent = self.detector.detect(command)

        destination = self.router.route(intent)

        entity = self.extractor.extract(command)

        search_engine = None
        search_query = None

        if intent == "SEARCH":
            search_engine, search_query = self.search_parser.parse(command)

        return {
            "command": command,
            "intent": intent,
            "entity": entity,
            "search_engine": search_engine,
            "search_query": search_query,
            "destination": destination
        }