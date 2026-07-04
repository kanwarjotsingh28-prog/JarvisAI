from backend.voice.voice_manager import VoiceManager
from backend.core.jarvis import JarvisCore


class Assistant:

    def __init__(self):

        self.voice = VoiceManager()
        self.jarvis = JarvisCore()

    def run(self):

        print("=" * 60)
        print("                 JARVIS AI")
        print("=" * 60)

        while True:

            print("\nListening...")

            command = self.voice.listen()

            if not command:
                continue

            print(f"\nYou: {command}")

            if command.lower() == "exit":
                break

            self.jarvis.execute(command)