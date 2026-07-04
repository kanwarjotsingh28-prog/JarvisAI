from backend.memory.memory_manager import MemoryManager
from backend.memory.memory_extractor import MemoryExtractor


class MemoryProcessor:

    def __init__(self):

        self.memory = MemoryManager()
        self.extractor = MemoryExtractor()

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

        if value is None:

            return "I don't know that yet."

        return value