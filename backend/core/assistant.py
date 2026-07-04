from backend.voice.voice_manager import VoiceManager
from backend.core.jarvis import JarvisCore


class Assistant:

    def __init__(self):

        self.voice = VoiceManager()
        self.jarvis = JarvisCore()

    def text_mode(self):

        print("\n===== TEXT MODE =====")

        while True:

            command = input("\nYou: ")

            if command.lower() == "exit":
                break

            result = self.jarvis.execute(command)

            if result.get("response"):
                print(f"\nJarvis: {result['response']}")

    def voice_mode(self):

        print("\n===== VOICE MODE =====")

        while True:

            print("\n🎤 Listening...")

            command = self.voice.listen()

            if not command:
                continue

            if command.lower() == "exit":
                break

            print(f"\nYou: {command}")

            result = self.jarvis.execute(command)

            if result.get("response"):
                print(f"\nJarvis: {result['response']}")

    def run(self):

        while True:

            print("\n" + "=" * 60)
            print("                    JARVIS AI")
            print("=" * 60)
            print("1. Voice Assistant")
            print("2. Text Assistant")
            print("3. Exit")

            choice = input("\nSelect Mode: ")

            if choice == "1":
                self.voice_mode()

            elif choice == "2":
                self.text_mode()

            elif choice == "3":
                print("\nGoodbye!")
                break

            else:
                print("\nInvalid option.")