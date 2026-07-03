from backend.core.command_processor import CommandProcessor


class JarvisCore:

    def __init__(self):

        self.processor = CommandProcessor()

    def execute(self, command):

        return self.processor.process(command)