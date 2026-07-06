from backend.memory.memory_manager import MemoryManager
from backend.memory.memory_extractor import MemoryExtractor
from backend.utils.logger import Logger


class MemoryProcessor:

    def __init__(self):

        self.memory = MemoryManager()
        self.extractor = MemoryExtractor()
        self.logger = Logger.get_logger()

    def save(self, command):

        data = self.extractor.extract(command)

        if data is None:
            return "I couldn't understand what to remember."

        self.memory.remember(
            data["key"],
            data["value"]
        )

        return "I'll remember that."

    def recall(self, key):

        value = self.memory.recall(key)

        return value