import pyttsx3


class Speaker:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 180)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()

        print("Starting...")

from backend.voice.speaker import Speaker

print("Imported")

speaker = Speaker()

print("Engine created")

speaker.speak("Hello Kanwarjot. I am Jarvis.")

print("Finished")