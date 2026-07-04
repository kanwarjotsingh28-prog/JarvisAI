from backend.voice.voice_manager import VoiceManager
from backend.core.jarvis import JarvisCore


class Assistant:

    def __init__(self):

        self.voice = VoiceManager()
        self.jarvis = JarvisCore()

    def run(self):

        print("=" * 60)
        print("                JARVIS AI")
        print("=" * 60)

        while True:

            mode = input("\nMode (voice/text): ").strip().lower()

            if mode == "voice":

                print("\nListening...")

                command = self.voice.listen()

            elif mode == "text":

                command = input("You: ")

            else:

                print("Please type 'voice' or 'text'.")
                continue

            if not command:
                continue

            if command.lower() == "exit":
                print("Goodbye!")
                break

            print(f"\nYou: {command}")

            result = self.jarvis.execute(command)

            if result.get("response"):
                print(f"\nJarvis: {result['response']}")