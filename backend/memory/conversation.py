class Conversation:

    def __init__(self):

        self.messages = []

    def add_user(self, text):

        self.messages.append({
            "role": "user",
            "content": text
        })

    def add_assistant(self, text):

        self.messages.append({
            "role": "assistant",
            "content": text
        })

    def history(self):

        return self.messages