from backend.voice.listener import Listener


class VoiceManager:

    def __init__(self):

        self.listener = Listener()

    def listen(self):

        return self.listener.listen()