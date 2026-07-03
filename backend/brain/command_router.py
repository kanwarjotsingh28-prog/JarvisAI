class CommandRouter:

    def route(self, intent):

        routes = {

            "OPEN_APPLICATION": "Automation Module",

            "SEARCH": "Search Module",

            "GET_TIME": "Time Module",

            "GET_WEATHER": "Weather Module",

            "SAVE_MEMORY": "Memory Module",

            "GREETING": "Conversation Module"

        }

        return routes.get(intent, "Unknown Module")