class IntentDetector:
    """
    Detects the user's intent from a text command.
    """

    def detect(self, command: str):

        command = command.lower()

        if any(word in command for word in ["open", "launch", "start"]):
            return "OPEN_APPLICATION"

        elif any(word in command for word in ["weather", "temperature"]):
            return "GET_WEATHER"

        elif any(word in command for word in ["time", "clock"]):
            return "GET_TIME"

        elif any(word in command for word in ["remember", "save"]):
            return "SAVE_MEMORY"

        elif any(word in command for word in ["hello", "hi", "hey"]):
            return "GREETING"

        else:
            return "UNKNOWN"