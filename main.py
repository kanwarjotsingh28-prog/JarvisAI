from backend.core.jarvis import JarvisCore


class Jarvis:

    def __init__(self):

        self.jarvis = JarvisCore()

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

            result = self.jarvis.execute(command)

            print("\nJarvis Analysis")
            print("-" * 40)
            print(f"Command        : {result['command']}")
            print(f"Intent         : {result['intent']}")
            print(f"Entity         : {result['entity']}")
            print(f"Search Engine  : {result['search_engine']}")
            print(f"Search Query   : {result['search_query']}")
            print(f"Destination    : {result['destination']}")
            if "response" in result:
               print()
               print(result["response"])
            print()

if __name__ == "__main__":

    jarvis = Jarvis()

    jarvis.start()