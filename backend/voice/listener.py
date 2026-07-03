from backend.voice.recorder import Recorder
from backend.voice.transcriber import Transcriber


class Listener:

    def __init__(self):

        self.recorder = Recorder()
        self.transcriber = Transcriber()

    def listen(self):

        audio = self.recorder.record()

        print("\n🧠 Processing...\n")

        text = self.transcriber.transcribe(audio)

        print(f"🗣 You said: {text}\n")

        return text