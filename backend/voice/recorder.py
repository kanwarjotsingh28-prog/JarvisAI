import os
import sounddevice as sd
from scipy.io.wavfile import write


class Recorder:

    def __init__(self):

        self.sample_rate = 16000

        self.output_path = os.path.join(
            "data",
            "audio",
            "command.wav"
        )

    def record(self, duration=3):

        print("\n🎤 Listening...")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(
            self.output_path,
            self.sample_rate,
            audio
        )

        return self.output_path