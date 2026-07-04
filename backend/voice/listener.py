from backend.voice.recorder import Recorder
from backend.voice.transcriber import Transcriber


class Listener:

    def __init__(self):

        self.recorder = Recorder()
        self.transcriber = Transcriber()

    def listen(self):

        audio = self.recorder.record(duration=3)

        print("\n🧠 Understanding...\n")

        text = self.transcriber.transcribe(audio)

        if text:

            text = text.strip()

            print(f"🗣 You said: {text}\n")

            return text

        return None