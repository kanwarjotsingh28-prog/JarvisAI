from backend.brain.brain import Brain
from backend.automation.automation import Automation


class Jarvis:

    def __init__(self):

        self.brain = Brain()
        self.automation = Automation()

    def start(self):

        print("=" * 60)
        print("          JARVIS AI v0.1")
        print("=" * 60)
        print("Type 'exit' to close JARVIS.\n")

        while True:

            command = input("You: ")

            if command.lower() == "exit":
                print("\nGoodbye!")
                break

            result = self.brain.think(command)

            print("\nJarvis Analysis")
            print("-" * 40)
            print(f"Command        : {result['command']}")
            print(f"Intent         : {result['intent']}")
            print(f"Entity         : {result['entity']}")
            print(f"Search Engine  : {result['search_engine']}")
            print(f"Search Query   : {result['search_query']}")
            print(f"Destination    : {result['destination']}")
            print()

            self.automation.execute(
                result["intent"],
                result["entity"],
                result["search_engine"],
                result["search_query"]
            )


if __name__ == "__main__":

    jarvis = Jarvis()

    jarvis.start()