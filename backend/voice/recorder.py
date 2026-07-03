import sounddevice as sd
from scipy.io.wavfile import write
import os


class Recorder:

    def __init__(self):

        self.sample_rate = 16000
        self.duration = 5

        self.output_path = os.path.join(
            "data",
            "audio",
            "command.wav"
        )

    def record(self):

        print("\n🎤 Recording...")

        audio = sd.rec(
            int(self.duration * self.sample_rate),
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

        print("✅ Recording complete.")

        return self.output_path