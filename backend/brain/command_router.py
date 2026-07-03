class CommandRouter:

    def route(self, intent):

        routes = {
            "OPEN_APPLICATION": "Automation Module",
            "GET_WEATHER": "Weather Module",
            "GET_TIME": "Clock Module",
            "SAVE_MEMORY": "Memory Module",
            "GREETING": "Conversation Module",
            "UNKNOWN": "Unknown Command"
        }

        return routes.get(intent, "Unknown Command")