mode = input("\nMode (voice/text): ").strip().lower()

if mode == "voice":
    command = self.voice.listen()
else:
    command = input("You: ")