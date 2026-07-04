def listen(self):

    audio = self.recorder.record(duration=3)

    print("🧠 Understanding...")

    text = self.transcriber.transcribe(audio)

    if text:

        text = text.strip()

        print(f"You said: {text}")

        return text

    return None